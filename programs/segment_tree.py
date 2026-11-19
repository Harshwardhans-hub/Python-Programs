"""Iterative segment tree for point replacement and inclusive range sums."""

from collections.abc import Iterable
from numbers import Real


class SegmentTree:
    """Maintain a numeric sequence with O(log n) updates and range queries."""

    def __init__(self, values: Iterable[Real] = ()) -> None:
        self._values = list(values)
        if any(isinstance(value, bool) or not isinstance(value, Real) for value in self._values):
            raise TypeError("values must be real numbers")
        self._size = 1
        while self._size < len(self._values):
            self._size *= 2
        self._tree: list[Real] = [0] * (2 * self._size)
        for index, value in enumerate(self._values):
            self._tree[self._size + index] = value
        for index in range(self._size - 1, 0, -1):
            self._tree[index] = self._tree[index * 2] + self._tree[index * 2 + 1]

    def __len__(self) -> int:
        return len(self._values)

    def _validate_index(self, index: int) -> None:
        if isinstance(index, bool) or not isinstance(index, int):
            raise TypeError("index must be an integer")
        if not 0 <= index < len(self._values):
            raise IndexError("index is outside the stored sequence")

    def update(self, index: int, value: Real) -> None:
        """Replace the value at index."""
        self._validate_index(index)
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("value must be a real number")
        self._values[index] = value
        position = self._size + index
        self._tree[position] = value
        position //= 2
        while position:
            self._tree[position] = self._tree[position * 2] + self._tree[position * 2 + 1]
            position //= 2

    def range_sum(self, start: int, end: int) -> Real:
        """Return the inclusive sum from start through end."""
        self._validate_index(start)
        self._validate_index(end)
        if start > end:
            raise IndexError("start cannot exceed end")
        left = self._size + start
        right = self._size + end + 1
        total: Real = 0
        while left < right:
            if left & 1:
                total += self._tree[left]
                left += 1
            if right & 1:
                right -= 1
                total += self._tree[right]
            left //= 2
            right //= 2
        return total
