"""Sequence algorithms using hash sets and one-pass scans."""

from collections.abc import Sequence
from numbers import Real


def longest_consecutive_sequence_length(values: Sequence[int]) -> int:
    """Return the longest run of consecutive integer values, in any order."""
    numbers = set(values)
    best = 0
    for number in numbers:
        if number - 1 not in numbers:
            current = number
            length = 1
            while current + 1 in numbers:
                current += 1
                length += 1
            best = max(best, length)
    return best


def majority_element(values: Sequence[int]) -> int | None:
    """Return a value appearing more than half the time, or None."""
    candidate = None
    count = 0
    for value in values:
        if count == 0:
            candidate = value
        count += 1 if value == candidate else -1
    if candidate is not None and values.count(candidate) > len(values) // 2:
        return candidate
    return None


def maximum_single_transaction_profit(prices: Sequence[Real]) -> Real:
    """Return the best non-negative buy-once/sell-once profit."""
    if not prices:
        return 0
    minimum = prices[0]
    best: Real = 0
    for price in prices[1:]:
        best = max(best, price - minimum)
        minimum = min(minimum, price)
    return best
