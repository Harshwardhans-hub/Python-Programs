"""Merge and insert closed numeric intervals."""

from collections.abc import Iterable


Interval = tuple[float, float]


def _validated(intervals: Iterable[tuple[float, float]]) -> list[Interval]:
    result: list[Interval] = []
    for interval in intervals:
        if not isinstance(interval, (tuple, list)) or len(interval) != 2:
            raise ValueError("each interval must contain exactly two endpoints")
        start, end = interval
        if start > end:
            raise ValueError("interval start cannot exceed interval end")
        result.append((start, end))
    return result


def merge_intervals(
    intervals: Iterable[tuple[float, float]],
    *,
    merge_touching: bool = True,
) -> list[Interval]:
    """Merge overlapping intervals, optionally merging adjacent endpoints."""
    ordered = sorted(_validated(intervals))
    if not ordered:
        return []
    merged: list[Interval] = [ordered[0]]

    for start, end in ordered[1:]:
        previous_start, previous_end = merged[-1]
        overlaps = start <= previous_end if merge_touching else start < previous_end
        if overlaps:
            merged[-1] = (previous_start, max(previous_end, end))
        else:
            merged.append((start, end))
    return merged


def insert_interval(
    intervals: Iterable[tuple[float, float]],
    new_interval: tuple[float, float],
    *,
    merge_touching: bool = True,
) -> list[Interval]:
    """Insert one interval and return the normalized merged result."""
    return merge_intervals(
        [*intervals, new_interval],
        merge_touching=merge_touching,
    )
