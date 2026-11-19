"""Small backtracking exercises for combinatorics and constraint solving."""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def subsets(values: Sequence[T]) -> list[list[T]]:
    """Return the power set; equal values at different positions remain distinct."""
    result: list[list[T]] = []
    current: list[T] = []

    def visit(index: int) -> None:
        if index == len(values):
            result.append(current.copy())
            return
        visit(index + 1)
        current.append(values[index])
        visit(index + 1)
        current.pop()

    visit(0)
    return result


def permutations(values: Sequence[T]) -> list[list[T]]:
    """Return all positional permutations in deterministic input order."""
    result: list[list[T]] = []
    current: list[T] = []
    used = [False] * len(values)

    def visit() -> None:
        if len(current) == len(values):
            result.append(current.copy())
            return
        for index, value in enumerate(values):
            if used[index]:
                continue
            used[index] = True
            current.append(value)
            visit()
            current.pop()
            used[index] = False

    visit()
    return result


def solve_n_queens(size: int) -> list[tuple[int, ...]]:
    """Return solutions as column positions, one per row, for an n×n board."""
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 1:
        raise ValueError("size must be at least 1")

    solutions: list[tuple[int, ...]] = []
    placement: list[int] = []
    occupied_columns: set[int] = set()
    descending_diagonals: set[int] = set()
    ascending_diagonals: set[int] = set()

    def place(row: int) -> None:
        if row == size:
            solutions.append(tuple(placement))
            return
        for column in range(size):
            descending = row - column
            ascending = row + column
            if (column in occupied_columns or descending in descending_diagonals
                    or ascending in ascending_diagonals):
                continue
            placement.append(column)
            occupied_columns.add(column)
            descending_diagonals.add(descending)
            ascending_diagonals.add(ascending)
            place(row + 1)
            placement.pop()
            occupied_columns.remove(column)
            descending_diagonals.remove(descending)
            ascending_diagonals.remove(ascending)

    place(0)
    return solutions
