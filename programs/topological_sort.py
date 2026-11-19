"""Kahn's algorithm for topological ordering of directed graphs."""

from collections import deque
from collections.abc import Iterable, Mapping
from typing import TypeVar

T = TypeVar("T")


def topological_sort(graph: Mapping[T, Iterable[T]]) -> list[T]:
    """Return a topological ordering, or raise ValueError when a cycle exists.

    Nodes that appear only as neighbors are included. Node order is stable
    relative to the order in which nodes and adjacency entries are encountered.
    """
    adjacency: dict[T, list[T]] = {}
    indegree: dict[T, int] = {}

    for node, neighbors in graph.items():
        adjacency.setdefault(node, [])
        indegree.setdefault(node, 0)
        for neighbor in neighbors:
            adjacency[node].append(neighbor)
            adjacency.setdefault(neighbor, [])
            indegree.setdefault(neighbor, 0)
            indegree[neighbor] += 1

    ready = deque(node for node, degree in indegree.items() if degree == 0)
    ordered: list[T] = []

    while ready:
        node = ready.popleft()
        ordered.append(node)
        for neighbor in adjacency[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                ready.append(neighbor)

    if len(ordered) != len(indegree):
        raise ValueError("graph contains a directed cycle")
    return ordered
