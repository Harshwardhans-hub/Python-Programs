"""Bipartite checks for undirected graphs represented by adjacency lists."""

from collections import deque
from collections.abc import Iterable, Mapping
from typing import TypeVar

T = TypeVar("T")


def is_bipartite(graph: Mapping[T, Iterable[T]]) -> bool:
    """Return whether an undirected graph can be colored with two colors.

    Adjacency is treated as undirected even when only one direction of an edge
    is listed. Neighbor-only and isolated vertices are included.
    """
    adjacency: dict[T, set[T]] = {}
    for node, neighbors in graph.items():
        adjacency.setdefault(node, set())
        for neighbor in neighbors:
            adjacency[node].add(neighbor)
            adjacency.setdefault(neighbor, set()).add(node)

    color: dict[T, int] = {}
    for start in adjacency:
        if start in color:
            continue
        color[start] = 0
        pending = deque([start])
        while pending:
            node = pending.popleft()
            for neighbor in adjacency[node]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[node]
                    pending.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
    return True
