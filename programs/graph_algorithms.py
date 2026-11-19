"""Breadth-first and depth-first traversal for adjacency-list graphs."""

from collections import deque
from collections.abc import Hashable, Iterable, Mapping
from typing import TypeVar

T = TypeVar("T", bound=Hashable)


def breadth_first_search(graph: Mapping[T, Iterable[T]], start: T) -> list[T]:
    """Return nodes reachable from start in breadth-first order."""
    visited = {start}
    order: list[T] = []
    pending = deque([start])

    while pending:
        node = pending.popleft()
        order.append(node)
        for neighbor in graph.get(node, ()):
            if neighbor not in visited:
                visited.add(neighbor)
                pending.append(neighbor)
    return order


def depth_first_search(graph: Mapping[T, Iterable[T]], start: T) -> list[T]:
    """Return nodes reachable from start in depth-first order.

    Neighbor order follows the order supplied in each adjacency iterable.
    """
    visited: set[T] = set()
    order: list[T] = []
    pending = [start]

    while pending:
        node = pending.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)
        neighbors = list(graph.get(node, ()))
        pending.extend(reversed(neighbors))
    return order


def has_path(graph: Mapping[T, Iterable[T]], start: T, target: T) -> bool:
    """Return whether target is reachable from start."""
    return target in breadth_first_search(graph, start)
