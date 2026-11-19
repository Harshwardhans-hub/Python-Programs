"""Prefix-sum helper for repeated inclusive range-sum queries."""

from collections.abc import Iterable
from numbers import Real


class PrefixSum:
    """Precompute cumulative sums to answer range queries in constant time."""

    def __init__(self, values: Iterable[Real]) -> None:
        self._prefix: list[Real] = [0]
        for value in values:
            if isinstance(value, bool) or not isinstance(value, Real):
                raise TypeError("values must be real numbers")
            self._prefix.append(self._prefix[-1] + value)

    def range_sum(self, start: int, end: int) -> Real:
        """Return the sum from start through end, with both bounds included."""
        if isinstance(start, bool) or not isinstance(start, int):
            raise TypeError("start must be an integer")
        if isinstance(end, bool) or not isinstance(end, int):
            raise TypeError("end must be an integer")
        size = len(self._prefix) - 1
        if start < 0 or end < start or end >= size:
            raise IndexError("range is outside the stored sequence")
        return self._prefix[end + 1] - self._prefix[start]

    def __len__(self) -> int:
        return len(self._prefix) - 1
