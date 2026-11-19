"""Bitwise exercises for non-negative integers."""

from collections.abc import Sequence


def count_set_bits(number: int) -> int:
    """Count the 1 bits in a non-negative integer."""
    _validate_non_negative(number)
    count = 0
    while number:
        number &= number - 1
        count += 1
    return count


def is_power_of_two(number: int) -> bool:
    """Return whether number is a positive power of two."""
    _validate_non_negative(number)
    return number > 0 and (number & (number - 1)) == 0


def single_number(values: Sequence[int]) -> int:
    """Return the value occurring once when every other value occurs twice."""
    result = 0
    for value in values:
        _validate_non_negative(value)
        result ^= value
    return result


def _validate_non_negative(number: int) -> None:
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 0:
        raise ValueError("number cannot be negative")
