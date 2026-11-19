"""Kruskal's algorithm for weighted undirected graphs."""

from collections.abc import Iterable
from numbers import Real
from typing import TypeVar

from programs.union_find import DisjointSet

T = TypeVar("T")


def minimum_spanning_forest(
    vertices: Iterable[T],
    edges: Iterable[tuple[T, T, Real]],
) -> tuple[list[tuple[T, T, Real]], Real]:
    """Return selected edges and total weight of a minimum spanning forest.

    Edges are (first, second, weight) triples. Negative weights are permitted.
    Disconnected input produces a minimum spanning forest rather than raising.
    """
    components = DisjointSet(vertices)
    normalized: list[tuple[T, T, Real]] = []

    for edge in edges:
        if not isinstance(edge, (tuple, list)) or len(edge) != 3:
            raise ValueError("each edge must contain two vertices and a weight")
        first, second, weight = edge
        if isinstance(weight, bool) or not isinstance(weight, Real):
            raise TypeError("edge weights must be real numbers")
        normalized.append((first, second, weight))

    selected: list[tuple[T, T, Real]] = []
    total: Real = 0
    for first, second, weight in sorted(normalized, key=lambda item: item[2]):
        if components.union(first, second):
            selected.append((first, second, weight))
            total += weight

    return selected, total
