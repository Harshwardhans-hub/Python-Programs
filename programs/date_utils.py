"""Simple date helpers implemented with the Python standard library."""

from datetime import date, timedelta
from collections.abc import Iterator, Iterable


def date_range(start: date, end: date) -> Iterator[date]:
    """Yield dates from *start* through *end*, including both endpoints."""
    if not isinstance(start, date) or not isinstance(end, date):
        raise TypeError("start and end must be date objects")
    if start > end:
        raise ValueError("start must not be after end")
    current = start
    while current <= end:
        yield current
        current += timedelta(days=1)


def count_business_days(start: date, end: date, holidays: Iterable[date] = ()) -> int:
    """Count weekdays in an inclusive date range, excluding supplied holidays."""
    holiday_set = set(holidays)
    return sum(
        1
        for current in date_range(start, end)
        if current.weekday() < 5 and current not in holiday_set
    )


def add_business_days(start: date, days: int, holidays: Iterable[date] = ()) -> date:
    """Move forward or backward by *days* weekdays, excluding supplied holidays."""
    if not isinstance(days, int):
        raise TypeError("days must be an integer")
    holiday_set = set(holidays)
    direction = 1 if days >= 0 else -1
    remaining = abs(days)
    current = start
    while remaining:
        current += timedelta(days=direction)
        if current.weekday() < 5 and current not in holiday_set:
            remaining -= 1
    return current
