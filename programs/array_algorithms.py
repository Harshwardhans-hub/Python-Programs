"""Classic array algorithms with non-mutating input contracts."""

from collections.abc import Sequence
from numbers import Real


def maximum_subarray_sum(values: Sequence[Real]) -> Real | None:
    """Return the largest contiguous-subarray sum using Kadane's algorithm."""
    if not values:
        return None
    if any(isinstance(value, bool) or not isinstance(value, Real) for value in values):
        raise TypeError("values must be real numbers")
    best_ending = best_overall = values[0]
    for value in values[1:]:
        best_ending = max(value, best_ending + value)
        best_overall = max(best_overall, best_ending)
    return best_overall


def product_except_self(values: Sequence[Real]) -> list[Real]:
    """Return products of all values except the value at each index."""
    result: list[Real] = [1] * len(values)
    prefix: Real = 1
    for index, value in enumerate(values):
        result[index] = prefix
        prefix *= value
    suffix: Real = 1
    for index in range(len(values) - 1, -1, -1):
        result[index] *= suffix
        suffix *= values[index]
    return result


def move_zeros_to_end(values: Sequence[Real]) -> list[Real]:
    """Return a copy with zeros moved to the end, preserving other order."""
    non_zero = [value for value in values if value != 0]
    return non_zero + [0] * (len(values) - len(non_zero))
