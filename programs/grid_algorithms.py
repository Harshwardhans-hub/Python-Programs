"""Grid traversal algorithms for rectangular matrices."""

from collections import deque
from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def _validate_grid(grid: Sequence[Sequence[T]]) -> tuple[int, int]:
    if not isinstance(grid, Sequence):
        raise TypeError("grid must be a sequence")
    if not grid:
        return 0, 0
    if any(not isinstance(row, Sequence) for row in grid):
        raise TypeError("grid rows must be sequences")
    columns = len(grid[0])
    if any(len(row) != columns for row in grid):
        raise ValueError("grid must be rectangular")
    return len(grid), columns


def flood_fill(
    grid: Sequence[Sequence[T]],
    start_row: int,
    start_column: int,
    new_value: T,
) -> list[list[T]]:
    """Return a copied grid with the starting cell's connected region recolored."""
    rows, columns = _validate_grid(grid)
    result = [list(row) for row in grid]
    if not rows or not columns:
        raise IndexError("cannot fill an empty grid")
    if not (0 <= start_row < rows and 0 <= start_column < columns):
        raise IndexError("starting cell is outside the grid")
    old_value = result[start_row][start_column]
    if old_value == new_value:
        return result

    pending = deque([(start_row, start_column)])
    result[start_row][start_column] = new_value
    while pending:
        row, column = pending.popleft()
        for next_row, next_column in (
            (row - 1, column), (row + 1, column),
            (row, column - 1), (row, column + 1),
        ):
            if (0 <= next_row < rows and 0 <= next_column < columns
                    and result[next_row][next_column] == old_value):
                result[next_row][next_column] = new_value
                pending.append((next_row, next_column))
    return result


def count_islands(grid: Sequence[Sequence[int]]) -> int:
    """Count 4-directionally connected groups of 1s in a binary grid."""
    rows, columns = _validate_grid(grid)
    visited: set[tuple[int, int]] = set()
    islands = 0

    for row in range(rows):
        for column in range(columns):
            if grid[row][column] not in (0, 1):
                raise ValueError("grid cells must be 0 or 1")
            if grid[row][column] == 0 or (row, column) in visited:
                continue
            islands += 1
            pending = [(row, column)]
            visited.add((row, column))
            while pending:
                current_row, current_column = pending.pop()
                for next_row, next_column in (
                    (current_row - 1, current_column),
                    (current_row + 1, current_column),
                    (current_row, current_column - 1),
                    (current_row, current_column + 1),
                ):
                    if (0 <= next_row < rows and 0 <= next_column < columns
                            and grid[next_row][next_column] == 1
                            and (next_row, next_column) not in visited):
                        visited.add((next_row, next_column))
                        pending.append((next_row, next_column))
    return islands
