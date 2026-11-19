"""Bellman-Ford shortest paths with reachable negative-cycle detection."""

from collections.abc import Iterable, Mapping
from numbers import Real
from typing import TypeVar

T = TypeVar("T")


def bellman_ford(
    graph: Mapping[T, Iterable[tuple[T, Real]]],
    start: T,
) -> dict[T, Real]:
    """Return shortest distances from start, supporting negative edge weights.

    Unreachable nodes are omitted. A negative cycle reachable from start raises
    ValueError because finite shortest-path distances do not exist.
    """
    edges: list[tuple[T, T, Real]] = []
    nodes: set[T] = {start}

    for node, neighbors in graph.items():
        nodes.add(node)
        for edge in neighbors:
            if not isinstance(edge, (tuple, list)) or len(edge) != 2:
                raise ValueError("each edge must contain a neighbor and weight")
            neighbor, weight = edge
            if isinstance(weight, bool) or not isinstance(weight, Real):
                raise TypeError("edge weights must be real numbers")
            edges.append((node, neighbor, weight))
            nodes.add(neighbor)

    distances: dict[T, Real] = {start: 0}
    for _ in range(max(0, len(nodes) - 1)):
        changed = False
        for source, target, weight in edges:
            if source not in distances:
                continue
            candidate = distances[source] + weight
            if candidate < distances.get(target, float("inf")):
                distances[target] = candidate
                changed = True
        if not changed:
            break

    for source, target, weight in edges:
        if source in distances and distances[source] + weight < distances.get(target, float("inf")):
            raise ValueError("graph contains a reachable negative-weight cycle")

    return distances
