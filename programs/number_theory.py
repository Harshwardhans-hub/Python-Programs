"""Number-theory exercises that complement the basic number utilities."""

from math import isqrt


def is_armstrong_number(number: int) -> bool:
    """Return whether a non-negative integer equals the sum of powered digits."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 0:
        return False
    digits = str(number)
    exponent = len(digits)
    return sum(int(digit) ** exponent for digit in digits) == number


def is_perfect_number(number: int) -> bool:
    """Return whether positive integer equals the sum of its proper divisors."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number <= 1:
        return False
    divisor_sum = 1
    for divisor in range(2, isqrt(number) + 1):
        if number % divisor == 0:
            divisor_sum += divisor
            paired = number // divisor
            if paired != divisor:
                divisor_sum += paired
    return divisor_sum == number


def is_leap_year(year: int) -> bool:
    """Apply the Gregorian leap-year rule."""
    if isinstance(year, bool) or not isinstance(year, int):
        raise TypeError("year must be an integer")
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def sum_of_digits(number: int) -> int:
    """Return the sum of decimal digits, ignoring a leading minus sign."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    return sum(int(digit) for digit in str(abs(number)))
