"""Heap-based selection and merging helpers."""

from collections.abc import Iterable
from heapq import merge, nlargest, nsmallest
from typing import TypeVar

T = TypeVar("T")


def top_k_largest(values: Iterable[T], count: int) -> list[T]:
    """Return up to count largest values in descending order."""
    if isinstance(count, bool) or not isinstance(count, int):
        raise TypeError("count must be an integer")
    if count < 0:
        raise ValueError("count cannot be negative")
    return nlargest(count, values)


def kth_smallest(values: Iterable[T], rank: int) -> T:
    """Return the one-based rank-th smallest value."""
    if isinstance(rank, bool) or not isinstance(rank, int):
        raise TypeError("rank must be an integer")
    if rank < 1:
        raise ValueError("rank must be at least 1")
    result = nsmallest(rank, values)
    if len(result) < rank:
        raise IndexError("rank exceeds the number of values")
    return result[-1]


def merge_sorted_sequences(*sequences: Iterable[T]) -> list[T]:
    """Merge already-sorted sequences into one sorted list."""
    return list(merge(*sequences))
