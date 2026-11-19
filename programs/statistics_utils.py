"""Dependency-free descriptive statistics for numeric sequences."""

import math
from numbers import Real
from collections.abc import Iterable


def _numeric_values(values: Iterable[Real]) -> list[float]:
    result: list[float] = []
    for value in values:
        if isinstance(value, bool) or not isinstance(value, Real):
            raise TypeError("all values must be real numbers")
        converted = float(value)
        if not math.isfinite(converted):
            raise ValueError("values must be finite")
        result.append(converted)
    if not result:
        raise ValueError("at least one value is required")
    return result


def mean(values: Iterable[Real]) -> float:
    """Return the arithmetic mean."""
    numbers = _numeric_values(values)
    return sum(numbers) / len(numbers)


def median(values: Iterable[Real]) -> float:
    """Return the median, averaging the middle pair for even-sized inputs."""
    numbers = sorted(_numeric_values(values))
    middle = len(numbers) // 2
    if len(numbers) % 2:
        return numbers[middle]
    return (numbers[middle - 1] + numbers[middle]) / 2


def population_variance(values: Iterable[Real]) -> float:
    """Return the population variance (dividing by N, not N - 1)."""
    numbers = _numeric_values(values)
    average = sum(numbers) / len(numbers)
    return sum((number - average) ** 2 for number in numbers) / len(numbers)


def population_std_dev(values: Iterable[Real]) -> float:
    """Return the population standard deviation."""
    return math.sqrt(population_variance(values))
