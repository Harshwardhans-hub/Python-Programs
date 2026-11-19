"""Combinatorics helpers for integer sequences."""

from collections.abc import Sequence
from math import comb


def pascal_triangle(rows: int) -> list[list[int]]:
    """Return the first rows of Pascal's triangle."""
    if isinstance(rows, bool) or not isinstance(rows, int):
        raise TypeError("rows must be an integer")
    if rows < 0:
        raise ValueError("rows cannot be negative")
    triangle: list[list[int]] = []
    for row_index in range(rows):
        if row_index == 0:
            triangle.append([1])
        else:
            previous = triangle[-1]
            row = [1]
            row.extend(previous[index - 1] + previous[index] for index in range(1, len(previous)))
            row.append(1)
            triangle.append(row)
    return triangle


def binomial_coefficient(n: int, k: int) -> int:
    """Return n choose k."""
    for name, value in (("n", n), ("k", k)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
    if n < 0 or k < 0:
        raise ValueError("n and k must be non-negative")
    if k > n:
        return 0
    return comb(n, k)


def combinations(values: Sequence[object], size: int) -> list[list[object]]:
    """Return positional combinations of the requested size."""
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size cannot be negative")
    if size > len(values):
        return []
    result: list[list[object]] = []
    current: list[object] = []

    def choose(start: int) -> None:
        if len(current) == size:
            result.append(current.copy())
            return
        remaining = size - len(current)
        for index in range(start, len(values) - remaining + 1):
            current.append(values[index])
            choose(index + 1)
            current.pop()

    choose(0)
    return result
