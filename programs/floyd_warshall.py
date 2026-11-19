"""Floyd-Warshall all-pairs shortest paths for weighted directed graphs."""

from collections.abc import Iterable, Mapping
from numbers import Real
from typing import TypeVar

T = TypeVar("T")


def floyd_warshall(
    graph: Mapping[T, Iterable[tuple[T, Real]]],
) -> dict[T, dict[T, Real]]:
    """Return shortest distances for every node pair.

    Unreachable pairs have math.inf distance. Negative edges are supported.
    Any negative cycle in the graph raises ValueError.
    """
    nodes: list[T] = list(graph)
    seen = set(nodes)
    edges: list[tuple[T, T, Real]] = []

    for source, neighbors in graph.items():
        for edge in neighbors:
            if not isinstance(edge, (tuple, list)) or len(edge) != 2:
                raise ValueError("each edge must contain a neighbor and weight")
            target, weight = edge
            if isinstance(weight, bool) or not isinstance(weight, Real):
                raise TypeError("edge weights must be real numbers")
            if target not in seen:
                seen.add(target)
                nodes.append(target)
            edges.append((source, target, weight))

    distance: dict[T, dict[T, Real]] = {
        source: {target: (0 if source == target else float("inf")) for target in nodes}
        for source in nodes
    }
    for source, target, weight in edges:
        distance[source][target] = min(distance[source][target], weight)

    for middle in nodes:
        for source in nodes:
            to_middle = distance[source][middle]
            if to_middle == float("inf"):
                continue
            for target in nodes:
                through = to_middle + distance[middle][target]
                if through < distance[source][target]:
                    distance[source][target] = through

    if any(distance[node][node] < 0 for node in nodes):
        raise ValueError("graph contains a negative-weight cycle")
    return distance
