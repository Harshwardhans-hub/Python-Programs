"""Greedy algorithm examples for scheduling and resource allocation."""

from collections.abc import Sequence
from numbers import Real


def select_activities(starts: Sequence[Real], ends: Sequence[Real]) -> list[int]:
    """Return indices of a maximum compatible activity set.

    Activities are treated as half-open intervals [start, end); an activity
    may begin when the previously selected activity ends.
    """
    if len(starts) != len(ends):
        raise ValueError("starts and ends must have equal lengths")
    activities: list[tuple[Real, Real, int]] = []
    for index, (start, end) in enumerate(zip(starts, ends)):
        if start > end:
            raise ValueError("activity start cannot exceed its end")
        activities.append((end, start, index))

    selected: list[int] = []
    last_finish: Real | None = None
    for end, start, index in sorted(activities):
        if last_finish is None or start >= last_finish:
            selected.append(index)
            last_finish = end
    return selected


def fractional_knapsack(
    weights: Sequence[Real],
    values: Sequence[Real],
    capacity: Real,
) -> float:
    """Return maximum value when items may be taken fractionally."""
    if len(weights) != len(values):
        raise ValueError("weights and values must have equal lengths")
    if capacity < 0:
        raise ValueError("capacity cannot be negative")
    if any(weight <= 0 for weight in weights):
        raise ValueError("weights must be positive")
    if any(isinstance(value, bool) or not isinstance(value, Real) for value in values):
        raise TypeError("values must be real numbers")

    items = sorted(
        ((value / weight, weight, value) for weight, value in zip(weights, values)),
        reverse=True,
    )
    remaining = float(capacity)
    total = 0.0
    for ratio, weight, value in items:
        if remaining <= 0:
            break
        taken = min(remaining, float(weight))
        total += float(ratio) * taken
        remaining -= taken
    return total
