"""Classic comparison sorts that return sorted copies of their input."""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def bubble_sort(values: Sequence[T]) -> list[T]:
    """Sort a copy using bubble sort with an early-exit optimization."""
    items = list(values)
    for end in range(len(items) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if items[index] > items[index + 1]:
                items[index], items[index + 1] = items[index + 1], items[index]
                swapped = True
        if not swapped:
            break
    return items


def insertion_sort(values: Sequence[T]) -> list[T]:
    """Sort a copy using stable insertion sort."""
    items = list(values)
    for index in range(1, len(items)):
        current = items[index]
        position = index
        while position > 0 and items[position - 1] > current:
            items[position] = items[position - 1]
            position -= 1
        items[position] = current
    return items


def selection_sort(values: Sequence[T]) -> list[T]:
    """Sort a copy by repeatedly selecting the smallest remaining item."""
    items = list(values)
    for start in range(len(items)):
        smallest = start
        for index in range(start + 1, len(items)):
            if items[index] < items[smallest]:
                smallest = index
        if smallest != start:
            items[start], items[smallest] = items[smallest], items[start]
    return items


def quick_sort(values: Sequence[T]) -> list[T]:
    """Return a sorted copy using a three-way quicksort partition."""
    items = list(values)
    if len(items) < 2:
        return items
    pivot = items[len(items) // 2]
    lower = [value for value in items if value < pivot]
    equal = [value for value in items if value == pivot]
    upper = [value for value in items if value > pivot]
    return quick_sort(lower) + equal + quick_sort(upper)
