"""Stack-based algorithms for strings and sequences."""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def balanced_brackets(text: str) -> bool:
    """Return whether (), [], and {} are balanced; ignore other characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    pairs = {")": "(", "]": "[", "}": "{"}
    opening = set(pairs.values())
    stack: list[str] = []
    for character in text:
        if character in opening:
            stack.append(character)
        elif character in pairs:
            if not stack or stack.pop() != pairs[character]:
                return False
    return not stack


def next_greater_elements(values: Sequence[T]) -> list[T | None]:
    """Return the next strictly greater value to the right for every item."""
    result: list[T | None] = [None] * len(values)
    pending: list[int] = []
    for index, value in enumerate(values):
        while pending and values[pending[-1]] < value:
            result[pending.pop()] = value
        pending.append(index)
    return result
