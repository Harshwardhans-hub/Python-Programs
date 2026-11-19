"""Beginner-friendly searching and sorting algorithms.

These helpers operate on in-memory sequences and never mutate the input.
"""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def linear_search(values: Sequence[T], target: T) -> int | None:
    """Return the first index containing target, or None when it is absent."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return None


def binary_search(values: Sequence[T], target: T) -> int | None:
    """Return the first matching index in an ascending sequence.

    The caller is responsible for supplying values sorted in non-decreasing
    order. Returning the first match makes duplicate handling deterministic.
    """
    low, high = 0, len(values)
    while low < high:
        middle = (low + high) // 2
        if values[middle] < target:
            low = middle + 1
        else:
            high = middle

    if low < len(values) and values[low] == target:
        return low
    return None


def merge_sort(values: Sequence[T]) -> list[T]:
    """Return a stable, sorted copy of values using merge sort."""
    items = list(values)
    if len(items) < 2:
        return items

    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])
    merged: list[T] = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged
