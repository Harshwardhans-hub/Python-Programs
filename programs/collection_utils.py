"""Small collection helpers for common Python practice problems."""

from collections.abc import Iterable, Sequence
from typing import Hashable, TypeVar

T = TypeVar("T", bound=Hashable)


def chunked(values: Sequence[T], size: int) -> list[list[T]]:
    """Split a sequence into consecutive lists of at most size elements."""
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size <= 0:
        raise ValueError("size must be greater than zero")
    return [list(values[index:index + size]) for index in range(0, len(values), size)]


def unique_preserving_order(values: Iterable[T]) -> list[T]:
    """Return unique hashable values in the order they first appear."""
    seen: set[T] = set()
    result: list[T] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def rotate_right(values: Sequence[T], steps: int = 1) -> list[T]:
    """Return a copy rotated right by steps positions.

    Negative steps rotate left. Empty sequences remain empty.
    """
    if isinstance(steps, bool) or not isinstance(steps, int):
        raise TypeError("steps must be an integer")
    items = list(values)
    if not items:
        return []
    shift = steps % len(items)
    if shift == 0:
        return items
    return items[-shift:] + items[:-shift]


def flatten_once(groups: Iterable[object]) -> list[object]:
    """Flatten one level of list/tuple nesting; leave other values unchanged."""
    result: list[object] = []
    for item in groups:
        if isinstance(item, (list, tuple)):
            result.extend(item)
        else:
            result.append(item)
    return result
