"""Tests for temperature and distance conversion helpers."""

import math
import unittest

from programs.conversion_utils import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    kilometers_to_miles,
    miles_to_kilometers,
)


class ConversionUtilsTests(unittest.TestCase):
    def test_temperature_reference_points(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)

    def test_distance_conversion_round_trip(self):
        self.assertAlmostEqual(kilometers_to_miles(10), 6.21371192237334)
        self.assertAlmostEqual(miles_to_kilometers(kilometers_to_miles(42)), 42)

    def test_negative_measurements_are_supported(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)

    def test_non_finite_and_non_numeric_values_are_rejected(self):
        for helper in (celsius_to_fahrenheit, fahrenheit_to_celsius, kilometers_to_miles, miles_to_kilometers):
            with self.subTest(helper=helper.__name__):
                with self.assertRaises(ValueError):
                    helper(math.inf)
                with self.assertRaises(TypeError):
                    helper("12")
                with self.assertRaises(TypeError):
                    helper(True)


if __name__ == "__main__":
    unittest.main()
