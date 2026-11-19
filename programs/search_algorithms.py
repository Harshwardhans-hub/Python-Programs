"""Searching algorithms for sorted sequences."""

from collections.abc import Sequence
from math import isqrt
from typing import TypeVar

T = TypeVar("T")


def jump_search(values: Sequence[T], target: T) -> int | None:
    """Return the first matching index using jump search.

    The input must be sorted in non-decreasing order.
    """
    size = len(values)
    if size == 0:
        return None
    step = max(1, isqrt(size))
    start = 0
    end = step

    while start < size and values[min(end, size) - 1] < target:
        start = end
        end += step
        if start >= size:
            return None

    for index in range(start, min(end, size)):
        if values[index] == target:
            return index
        if values[index] > target:
            break
    return None


def exponential_search(values: Sequence[T], target: T) -> int | None:
    """Return the first matching index using exponential range growth."""
    size = len(values)
    if size == 0 or values[0] > target:
        return None
    if values[0] == target:
        return 0

    bound = 1
    while bound < size and values[bound] < target:
        bound *= 2

    low = bound // 2
    high = min(bound, size - 1)
    left, right = low, high + 1
    while left < right:
        middle = (left + right) // 2
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle
    return left if left < size and values[left] == target else None
