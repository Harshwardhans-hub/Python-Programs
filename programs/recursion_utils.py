"""Small recursive exercises with explicit input validation."""

from collections.abc import Sequence
from numbers import Real


def factorial(number: int) -> int:
    """Return n! for a non-negative integer."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 0:
        raise ValueError("factorial is undefined for negative integers")
    if number < 2:
        return 1
    return number * factorial(number - 1)


def power(base: Real, exponent: int) -> Real:
    """Raise base to an integer exponent using exponentiation by squaring."""
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent < 0:
        if base == 0:
            raise ZeroDivisionError("zero cannot be raised to a negative power")
        return 1 / power(base, -exponent)
    if exponent == 0:
        return 1
    half = power(base, exponent // 2)
    squared = half * half
    return squared if exponent % 2 == 0 else base * squared


def sum_nested(values: Sequence[object]) -> Real:
    """Sum numeric values in arbitrarily nested lists and tuples."""
    if not isinstance(values, (list, tuple)):
        raise TypeError("values must be a list or tuple")
    total: Real = 0
    for value in values:
        if isinstance(value, (list, tuple)):
            total += sum_nested(value)
        elif isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("nested values must be real numbers or sequences")
        else:
            total += value
    return total
