"""Fenwick tree (binary indexed tree) for point updates and prefix sums."""

from collections.abc import Iterable
from numbers import Real


class FenwickTree:
    """Maintain numeric values with O(log n) updates and prefix queries."""

    def __init__(self, values: Iterable[Real] = ()) -> None:
        self._values = list(values)
        if any(isinstance(value, bool) or not isinstance(value, Real) for value in self._values):
            raise TypeError("values must be real numbers")
        self._tree: list[Real] = [0] + self._values.copy()
        for index in range(1, len(self._tree)):
            parent = index + (index & -index)
            if parent < len(self._tree):
                self._tree[parent] += self._tree[index]

    def __len__(self) -> int:
        return len(self._values)

    def _validate_index(self, index: int) -> None:
        if isinstance(index, bool) or not isinstance(index, int):
            raise TypeError("index must be an integer")
        if not 0 <= index < len(self._values):
            raise IndexError("index is outside the stored sequence")

    def add(self, index: int, delta: Real) -> None:
        """Add delta to the value at index."""
        self._validate_index(index)
        if isinstance(delta, bool) or not isinstance(delta, Real):
            raise TypeError("delta must be a real number")
        self._values[index] += delta
        position = index + 1
        while position < len(self._tree):
            self._tree[position] += delta
            position += position & -position

    def prefix_sum(self, end: int) -> Real:
        """Return sum of values from index 0 through end; -1 returns zero."""
        if isinstance(end, bool) or not isinstance(end, int):
            raise TypeError("end must be an integer")
        if end == -1:
            return 0
        self._validate_index(end)
        total: Real = 0
        position = end + 1
        while position:
            total += self._tree[position]
            position -= position & -position
        return total

    def range_sum(self, start: int, end: int) -> Real:
        """Return inclusive range sum from start through end."""
        self._validate_index(start)
        self._validate_index(end)
        if start > end:
            raise IndexError("start cannot exceed end")
        return self.prefix_sum(end) - self.prefix_sum(start - 1)
