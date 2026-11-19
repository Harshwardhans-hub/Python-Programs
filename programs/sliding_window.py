"""Linear-time sliding-window exercises."""

from collections import defaultdict
from collections.abc import Sequence
from numbers import Real


def maximum_subarray_sum(values: Sequence[Real], window_size: int) -> Real | None:
    """Return the largest sum of a fixed-size contiguous window.

    Return None when the requested window is larger than the sequence.
    """
    if isinstance(window_size, bool) or not isinstance(window_size, int):
        raise TypeError("window_size must be an integer")
    if window_size <= 0:
        raise ValueError("window_size must be positive")
    if window_size > len(values):
        return None
    if any(isinstance(value, bool) or not isinstance(value, Real) for value in values):
        raise TypeError("values must be real numbers")

    current = sum(values[:window_size])
    best = current
    for index in range(window_size, len(values)):
        current += values[index] - values[index - window_size]
        best = max(best, current)
    return best


def longest_unique_substring_length(text: str) -> int:
    """Return the length of the longest substring with all distinct characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    last_seen: dict[str, int] = {}
    left = best = 0
    for right, char in enumerate(text):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1
        last_seen[char] = right
        best = max(best, right - left + 1)
    return best


def count_subarrays_with_sum(values: Sequence[int], target: int) -> int:
    """Count contiguous subarrays with the exact target sum, including negatives."""
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1
    running = matches = 0
    for value in values:
        running += value
        matches += prefix_counts[running - target]
        prefix_counts[running] += 1
    return matches
