"""Deque-based algorithms for queue and window practice."""

from collections import deque
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def sliding_window_maximum(values: Sequence[T], window_size: int) -> list[T]:
    """Return the maximum of each contiguous window in linear time."""
    if isinstance(window_size, bool) or not isinstance(window_size, int):
        raise TypeError("window_size must be an integer")
    if window_size <= 0:
        raise ValueError("window_size must be positive")
    if window_size > len(values):
        return []

    candidates: deque[int] = deque()
    result: list[T] = []
    for index, value in enumerate(values):
        while candidates and candidates[0] <= index - window_size:
            candidates.popleft()
        while candidates and values[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(index)
        if index >= window_size - 1:
            result.append(values[candidates[0]])
    return result
