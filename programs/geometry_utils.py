"""Basic two-dimensional geometry helpers."""

from math import hypot
from numbers import Real


Point = tuple[Real, Real]


def _validate_point(point: Point, name: str) -> None:
    if not isinstance(point, (tuple, list)) or len(point) != 2:
        raise ValueError(f"{name} must contain exactly two coordinates")
    if any(isinstance(value, bool) or not isinstance(value, Real) for value in point):
        raise TypeError(f"{name} coordinates must be real numbers")


def euclidean_distance(first: Point, second: Point) -> float:
    """Return straight-line distance between two 2D points."""
    _validate_point(first, "first")
    _validate_point(second, "second")
    return hypot(float(first[0] - second[0]), float(first[1] - second[1]))


def manhattan_distance(first: Point, second: Point) -> Real:
    """Return the sum of absolute coordinate differences."""
    _validate_point(first, "first")
    _validate_point(second, "second")
    return abs(first[0] - second[0]) + abs(first[1] - second[1])


def point_in_rectangle(
    point: Point,
    lower_left: Point,
    upper_right: Point,
    *,
    inclusive: bool = True,
) -> bool:
    """Check whether point lies inside an axis-aligned rectangle."""
    for value, name in ((point, "point"), (lower_left, "lower_left"), (upper_right, "upper_right")):
        _validate_point(value, name)
    if lower_left[0] > upper_right[0] or lower_left[1] > upper_right[1]:
        raise ValueError("rectangle bounds are reversed")
    if inclusive:
        return (
            lower_left[0] <= point[0] <= upper_right[0]
            and lower_left[1] <= point[1] <= upper_right[1]
        )
    return (
        lower_left[0] < point[0] < upper_right[0]
        and lower_left[1] < point[1] < upper_right[1]
    )
