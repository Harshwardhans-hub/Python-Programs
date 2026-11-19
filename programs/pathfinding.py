"""Shortest path search on rectangular grids with blocked cells."""

from collections import deque
from collections.abc import Sequence


Coordinate = tuple[int, int]


def shortest_grid_path(
    grid: Sequence[Sequence[int]],
    start: Coordinate,
    target: Coordinate,
) -> list[Coordinate] | None:
    """Return a shortest 4-directional path through 0 cells, including endpoints.

    Cells with value 1 are blocked. Return None when no route exists.
    """
    if not isinstance(grid, Sequence):
        raise TypeError("grid must be a sequence")
    if not grid:
        raise ValueError("grid cannot be empty")
    if any(not isinstance(row, Sequence) for row in grid):
        raise TypeError("grid rows must be sequences")
    columns = len(grid[0])
    if columns == 0 or any(len(row) != columns for row in grid):
        raise ValueError("grid must be non-empty and rectangular")
    if any(cell not in (0, 1) for row in grid for cell in row):
        raise ValueError("grid cells must be 0 or 1")

    rows = len(grid)
    for coordinate in (start, target):
        if (not isinstance(coordinate, tuple) or len(coordinate) != 2
                or any(isinstance(value, bool) or not isinstance(value, int) for value in coordinate)):
            raise TypeError("coordinates must be pairs of integers")
        row, column = coordinate
        if not (0 <= row < rows and 0 <= column < columns):
            raise IndexError("coordinate is outside the grid")

    if grid[start[0]][start[1]] == 1 or grid[target[0]][target[1]] == 1:
        return None

    pending = deque([start])
    parent: dict[Coordinate, Coordinate | None] = {start: None}
    while pending:
        current = pending.popleft()
        if current == target:
            path: list[Coordinate] = []
            position: Coordinate | None = current
            while position is not None:
                path.append(position)
                position = parent[position]
            return list(reversed(path))
        row, column = current
        for next_cell in ((row - 1, column), (row + 1, column),
                          (row, column - 1), (row, column + 1)):
            next_row, next_column = next_cell
            if (0 <= next_row < rows and 0 <= next_column < columns
                    and grid[next_row][next_column] == 0
                    and next_cell not in parent):
                parent[next_cell] = current
                pending.append(next_cell)
    return None
