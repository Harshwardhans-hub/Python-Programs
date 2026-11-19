"""Two-pointer patterns for sorted arrays and text."""

from collections.abc import Sequence
from numbers import Real


def two_sum_sorted(values: Sequence[Real], target: Real) -> tuple[int, int] | None:
    """Return zero-based indices of a pair summing to target, or None.

    The input must be sorted in non-decreasing order. The returned indices
    always refer to the original input sequence.
    """
    left, right = 0, len(values) - 1
    while left < right:
        total = values[left] + values[right]
        if total == target:
            return left, right
        if total < target:
            left += 1
        else:
            right -= 1
    return None


def unique_sorted_values(values: Sequence[Real]) -> list[Real]:
    """Return a sorted sequence with adjacent duplicates removed."""
    result: list[Real] = []
    for value in values:
        if not result or value != result[-1]:
            result.append(value)
    return result


def is_text_palindrome(text: str) -> bool:
    """Check a palindrome while ignoring case and non-alphanumeric characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    left, right = 0, len(text) - 1
    while left < right:
        while left < right and not text[left].isalnum():
            left += 1
        while left < right and not text[right].isalnum():
            right -= 1
        if text[left].casefold() != text[right].casefold():
            return False
        left += 1
        right -= 1
    return True
