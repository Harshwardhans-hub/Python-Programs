"""Common temperature and distance conversions."""

import math


def _require_finite_number(value: float, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be an int or float")
    if not math.isfinite(value):
        raise ValueError(f"{name} must be finite")


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert degrees Celsius to degrees Fahrenheit."""
    _require_finite_number(celsius, "celsius")
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert degrees Fahrenheit to degrees Celsius."""
    _require_finite_number(fahrenheit, "fahrenheit")
    return (fahrenheit - 32) * 5 / 9


def kilometers_to_miles(kilometers: float) -> float:
    """Convert kilometers to miles."""
    _require_finite_number(kilometers, "kilometers")
    return kilometers * 0.621371192237334


def miles_to_kilometers(miles: float) -> float:
    """Convert miles to kilometers."""
    _require_finite_number(miles, "miles")
    return miles / 0.621371192237334
