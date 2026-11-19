"""0-1 BFS for graphs whose edge weights are only zero or one."""

from collections import deque
from collections.abc import Iterable, Mapping
from typing import TypeVar

T = TypeVar("T")


def zero_one_bfs(
    graph: Mapping[T, Iterable[tuple[T, int]]],
    start: T,
) -> dict[T, int]:
    """Return shortest distances from start using a double-ended queue.

    Edges must have integer weights exactly equal to 0 or 1. Unreachable nodes
    are omitted from the returned dictionary.
    """
    adjacency: dict[T, list[tuple[T, int]]] = {}
    for node, edges in graph.items():
        adjacency.setdefault(node, [])
        for edge in edges:
            if not isinstance(edge, (tuple, list)) or len(edge) != 2:
                raise ValueError("each edge must contain a neighbor and weight")
            neighbor, weight = edge
            if isinstance(weight, bool) or not isinstance(weight, int):
                raise TypeError("edge weights must be integers")
            if weight not in (0, 1):
                raise ValueError("edge weights must be either 0 or 1")
            adjacency[node].append((neighbor, weight))
            adjacency.setdefault(neighbor, [])

    distances = {start: 0}
    pending = deque([start])
    while pending:
        node = pending.popleft()
        current_distance = distances[node]
        for neighbor, weight in adjacency.get(node, ()):
            candidate = current_distance + weight
            if candidate < distances.get(neighbor, float("inf")):
                distances[neighbor] = candidate
                if weight == 0:
                    pending.appendleft(neighbor)
                else:
                    pending.append(neighbor)
    return distances
