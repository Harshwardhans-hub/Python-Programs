"""Cycle detection helpers for directed and undirected graphs."""

from collections.abc import Iterable, Mapping
from typing import TypeVar

from programs.union_find import DisjointSet

T = TypeVar("T")


def has_directed_cycle(graph: Mapping[T, Iterable[T]]) -> bool:
    """Return whether a directed graph contains a back edge.

    Nodes that appear only as neighbors are included. Uses iterative DFS to
    avoid Python recursion-depth limits on long directed chains.
    """
    adjacency: dict[T, list[T]] = {}
    for node, neighbors in graph.items():
        adjacency.setdefault(node, [])
        for neighbor in neighbors:
            adjacency[node].append(neighbor)
            adjacency.setdefault(neighbor, [])

    # 0 = unseen, 1 = currently on the DFS path, 2 = fully processed.
    color: dict[T, int] = {node: 0 for node in adjacency}
    for start in adjacency:
        if color[start] != 0:
            continue
        color[start] = 1
        stack: list[tuple[T, object]] = [(start, iter(adjacency[start]))]
        while stack:
            node, neighbors = stack[-1]
            try:
                neighbor = next(neighbors)  # type: ignore[arg-type]
            except StopIteration:
                color[node] = 2
                stack.pop()
                continue
            if color[neighbor] == 1:
                return True
            if color[neighbor] == 0:
                color[neighbor] = 1
                stack.append((neighbor, iter(adjacency[neighbor])))
    return False


def has_undirected_cycle(
    vertices: Iterable[T],
    edges: Iterable[tuple[T, T]],
) -> bool:
    """Return whether an undirected edge list contains a cycle.

    Self-loops and repeated parallel edges count as cycles. Isolated vertices
    are accepted and do not affect the result.
    """
    components = DisjointSet(vertices)
    for edge in edges:
        if not isinstance(edge, (tuple, list)) or len(edge) != 2:
            raise ValueError("each edge must contain exactly two vertices")
        first, second = edge
        if not components.union(first, second):
            return True
    return False
