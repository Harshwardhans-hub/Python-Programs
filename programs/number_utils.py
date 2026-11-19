"""Small, dependency-free helpers for common number exercises."""


def _require_int(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def is_prime(number: int) -> bool:
    """Return whether *number* is prime; values below 2 are not prime."""
    _require_int(number, "number")
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def fibonacci_terms(count: int) -> list[int]:
    """Return the first *count* Fibonacci terms, starting with 0, 1."""
    _require_int(count, "count")
    if count < 0:
        raise ValueError("count cannot be negative")
    terms: list[int] = []
    first, second = 0, 1
    for _ in range(count):
        terms.append(first)
        first, second = second, first + second
    return terms


def greatest_common_divisor(first: int, second: int) -> int:
    """Return the non-negative greatest common divisor of two integers."""
    _require_int(first, "first")
    _require_int(second, "second")
    first, second = abs(first), abs(second)
    while second:
        first, second = second, first % second
    return first


def least_common_multiple(first: int, second: int) -> int:
    """Return the non-negative least common multiple; zero if either input is 0."""
    _require_int(first, "first")
    _require_int(second, "second")
    if first == 0 or second == 0:
        return 0
    return abs(first // greatest_common_divisor(first, second) * second)
