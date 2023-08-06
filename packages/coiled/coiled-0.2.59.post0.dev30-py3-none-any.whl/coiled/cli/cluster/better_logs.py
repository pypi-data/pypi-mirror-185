import sys
import time
from typing import Optional

import click
from rich.console import Console

import coiled

from ..utils import CONTEXT_SETTINGS

COLORS = [
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
]


@click.command(
    context_settings=CONTEXT_SETTINGS,
)
@click.option(
    "--account",
    default=None,
    help="Coiled account (uses default account if not specified)",
)
@click.option(
    "--cluster",
    default=None,
    help="Cluster for which to show logs, default is most recent",
)
@click.option(
    "--instance-ids",
    default=None,
    help="Only show logs for instances matching these pk ids",
)
@click.option(
    "--system",
    default=False,
    is_flag=True,
    help="Just show system logs",
)
@click.option(
    "--combined",
    default=False,
    is_flag=True,
    help="Show combined system and dask logs",
)
@click.option(
    "--tail",
    default=False,
    is_flag=True,
    help="Keep tailing logs",
)
@click.option(
    "--color",
    default=False,
    is_flag=True,
    help="Use for color in logs",
)
@click.option(
    "--interval",
    default=3,
    help="Tail polling interval",
)
def better_logs(
    account: Optional[str],
    cluster: Optional[str],
    instance_ids: Optional[str],  # TODO easily select scheduler / workers
    system: bool,
    combined: bool,
    tail: bool,
    interval: int,
    color: bool,
):
    dask = not system or combined
    system = system or combined

    # convert "123,456" to [123, 456]
    instance_pk_ids = list(map(int, instance_ids.split(","))) if instance_ids else None

    if cluster and cluster.isnumeric():
        cluster_id = int(cluster)
    elif cluster:
        # get cluster by name

        try:
            with coiled.Cloud(account=account) as cloud:
                clusters = cloud.get_clusters_by_name(name=cluster)
            if clusters:
                recent_cluster = clusters[-1]
            else:
                raise click.ClickException(
                    f"Unable to find cluster with name '{cluster}'"
                )

            if tail and recent_cluster["current_state"]["state"] in (
                "stopped",
                "error",
            ):
                tail = False
                print(
                    f"[red]Cluster state is {recent_cluster['current_state']['state']} so not tailing.[/red]",
                    file=sys.stderr,
                )

            cluster_id = recent_cluster["id"]

        except coiled.errors.DoesNotExist:
            cluster_id = None
    else:
        # default to most recent cluster
        clusters = coiled.list_clusters(max_pages=1)
        if not clusters:
            raise ValueError("Unable to find any clusters for your account")
        match = max(clusters, key=lambda c: c["id"])
        cluster_id = match["id"]

    if not cluster_id:
        raise click.ClickException(f"Unable to find cluster `{cluster}`")

    console = Console(force_terminal=color)

    console.print(f"=== Logs for cluster {cluster_id} ===\n")

    last_timestamp = None
    last_events = set()
    if tail:
        # for tail, start with logs from 30s ago
        current_ms = int(time.time_ns() // 1e6)
        last_timestamp = current_ms - (30 * 1000)

    while True:
        events = coiled.better_cluster_logs(
            cluster_id=cluster_id,
            instance_ids=instance_pk_ids,
            dask=dask,
            system=system,
            since_ms=last_timestamp,
        )

        if last_events:
            events = [
                e
                for e in events
                if e["timestamp"] != last_timestamp
                or event_dedupe_key(e) not in last_events
            ]

        if events:
            print_events(console, events)

            last_timestamp = events[-1]["timestamp"]
            last_events = {
                event_dedupe_key(e) for e in events if e["timestamp"] == last_timestamp
            }

        if tail:
            # TODO stop tailing once cluster is stopped/errored (future MR)
            time.sleep(interval)
        else:
            break


def match_cluster(clusters: list[dict], cluster: str) -> dict:
    if cluster.isnumeric():
        matches = [c for c in clusters if c["id"] == int(cluster)]
        if len(matches) == 1:
            return matches[0]
        elif len(matches) > 1:
            raise ValueError(f"Multiple clusters match '{cluster}'")

    # try to match on cluster name
    matches = sorted(
        [c for c in clusters if c["name"] == cluster], key=lambda c: c["id"]
    )
    if matches:
        return matches[-1]

    raise ValueError(f"No clusters match '{cluster}'")


def event_dedupe_key(event):
    return f'{event["timestamp"]}#{event["instance_id"]}#{event["message"]}'


def print_events(console, events, pretty=True):
    for e in events:
        console.print(format_log_event(e, pretty=pretty))


def format_log_event(event, pretty=True):

    message = event["message"]

    # indent multiline tracebacks
    if "\n" in message and "Traceback" in message:
        message = message.replace("\n", "\n  ")

    if pretty:
        color = COLORS[event["instance_id"] % len(COLORS)]
        return f"[{color}]({event['instance_id']})[/{color}] {message}"
    else:
        return f"({event['instance_id']}) {message}"
