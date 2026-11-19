"""Disjoint-set union (union-find) with path compression and union by rank."""

from collections.abc import Iterable
from typing import Generic, Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


class DisjointSet(Generic[T]):
    """Track a partition of values into disjoint connected components."""

    def __init__(self, values: Iterable[T] = ()) -> None:
        self._parent: dict[T, T] = {}
        self._rank: dict[T, int] = {}
        self._components = 0
        for value in values:
            self.add(value)

    def add(self, value: T) -> None:
        if value not in self._parent:
            self._parent[value] = value
            self._rank[value] = 0
            self._components += 1

    def find(self, value: T) -> T:
        """Return the representative for value, adding unseen values."""
        self.add(value)
        if self._parent[value] != value:
            self._parent[value] = self.find(self._parent[value])
        return self._parent[value]

    def union(self, first: T, second: T) -> bool:
        """Join two components; return True only when a merge occurred."""
        root_first = self.find(first)
        root_second = self.find(second)
        if root_first == root_second:
            return False
        if self._rank[root_first] < self._rank[root_second]:
            root_first, root_second = root_second, root_first
        self._parent[root_second] = root_first
        if self._rank[root_first] == self._rank[root_second]:
            self._rank[root_first] += 1
        self._components -= 1
        return True

    def connected(self, first: T, second: T) -> bool:
        return self.find(first) == self.find(second)

    @property
    def component_count(self) -> int:
        return self._components
