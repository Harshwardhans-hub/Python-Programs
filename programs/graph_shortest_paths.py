"""Dijkstra shortest paths for graphs with non-negative edge weights."""

from heapq import heappop, heappush
from collections.abc import Iterable, Mapping
from numbers import Real
from typing import TypeVar

T = TypeVar("T")


def dijkstra(
    graph: Mapping[T, Iterable[tuple[T, Real]]],
    start: T,
) -> dict[T, Real]:
    """Return shortest distances from start to every reachable node.

    Edges are represented as (neighbor, weight) pairs. Negative weights are
    rejected because Dijkstra's algorithm does not support them.
    """
    distances: dict[T, Real] = {start: 0}
    pending: list[tuple[Real, int, T]] = [(0, 0, start)]
    sequence = 1

    while pending:
        distance, _, node = heappop(pending)
        if distance != distances.get(node):
            continue
        for neighbor, weight in graph.get(node, ()):
            if isinstance(weight, bool) or not isinstance(weight, Real):
                raise TypeError("edge weights must be real numbers")
            if weight < 0:
                raise ValueError("Dijkstra requires non-negative edge weights")
            candidate = distance + weight
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                heappush(pending, (candidate, sequence, neighbor))
                sequence += 1
    return distances
