"""Additional graph algorithms for directed and unweighted graphs."""

from collections import deque
from collections.abc import Iterable, Mapping
from typing import TypeVar

T = TypeVar("T")


def topological_sort(graph: Mapping[T, Iterable[T]]) -> list[T]:
    """Return a topological ordering or raise ValueError when a cycle exists."""
    nodes = list(graph)
    known = set(nodes)
    adjacency: dict[T, list[T]] = {}
    for node, neighbors in graph.items():
        adjacency[node] = list(neighbors)
        for neighbor in adjacency[node]:
            if neighbor not in known:
                known.add(neighbor)
                nodes.append(neighbor)

    indegree = {node: 0 for node in nodes}
    for neighbors in adjacency.values():
        for neighbor in neighbors:
            indegree[neighbor] += 1

    ready = deque(node for node in nodes if indegree[node] == 0)
    result: list[T] = []
    while ready:
        node = ready.popleft()
        result.append(node)
        for neighbor in adjacency.get(node, ()):
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                ready.append(neighbor)

    if len(result) != len(nodes):
        raise ValueError("graph contains a directed cycle")
    return result


def shortest_unweighted_path(
    graph: Mapping[T, Iterable[T]],
    start: T,
    target: T,
) -> list[T] | None:
    """Return a shortest path as nodes, or None when target is unreachable."""
    pending = deque([start])
    parent: dict[T, T | None] = {start: None}

    while pending:
        node = pending.popleft()
        if node == target:
            path: list[T] = []
            current: T | None = node
            while current is not None:
                path.append(current)
                current = parent[current]
            return list(reversed(path))
        for neighbor in graph.get(node, ()):
            if neighbor not in parent:
                parent[neighbor] = node
                pending.append(neighbor)
    return None
