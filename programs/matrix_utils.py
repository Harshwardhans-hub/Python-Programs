"""Basic matrix operations with shape validation and no input mutation."""

from collections.abc import Sequence
from numbers import Real


Matrix = Sequence[Sequence[Real]]


def _dimensions(matrix: Matrix, name: str) -> tuple[int, int]:
    if not isinstance(matrix, Sequence):
        raise TypeError(f"{name} must be a sequence of rows")
    if not matrix:
        return 0, 0
    if any(not isinstance(row, Sequence) for row in matrix):
        raise TypeError(f"{name} must contain row sequences")
    columns = len(matrix[0])
    if any(len(row) != columns for row in matrix):
        raise ValueError(f"{name} must be rectangular")
    for row in matrix:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, Real):
                raise TypeError(f"{name} entries must be real numbers")
    return len(matrix), columns


def transpose(matrix: Matrix) -> list[list[Real]]:
    """Return rows and columns exchanged."""
    rows, columns = _dimensions(matrix, "matrix")
    return [[matrix[row][column] for row in range(rows)] for column in range(columns)]


def add_matrices(first: Matrix, second: Matrix) -> list[list[Real]]:
    """Add matrices with identical dimensions."""
    first_rows, first_columns = _dimensions(first, "first")
    second_rows, second_columns = _dimensions(second, "second")
    if (first_rows, first_columns) != (second_rows, second_columns):
        raise ValueError("matrices must have identical dimensions")
    return [
        [first[r][c] + second[r][c] for c in range(first_columns)]
        for r in range(first_rows)
    ]


def multiply_matrices(first: Matrix, second: Matrix) -> list[list[Real]]:
    """Multiply matrices when columns(first) equals rows(second)."""
    first_rows, first_columns = _dimensions(first, "first")
    second_rows, second_columns = _dimensions(second, "second")
    if first_columns != second_rows:
        raise ValueError("first matrix columns must equal second matrix rows")
    if first_rows == 0 or second_columns == 0:
        return []
    return [
        [
            sum(first[r][k] * second[k][c] for k in range(first_columns))
            for c in range(second_columns)
        ]
        for r in range(first_rows)
    ]


def rotate_clockwise(matrix: Matrix) -> list[list[Real]]:
    """Return a 90-degree clockwise rotation of a rectangular matrix."""
    return [list(reversed(row)) for row in transpose(matrix)]
