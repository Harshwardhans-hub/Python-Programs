"""Tests for recursive factorial, exponentiation, and nested sums."""

import unittest

from programs.recursion_utils import factorial, power, sum_nested


class RecursionUtilsTests(unittest.TestCase):
    def test_factorial_values(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)

    def test_factorial_rejects_invalid_inputs(self):
        with self.assertRaises(ValueError):
            factorial(-1)
        with self.assertRaises(TypeError):
            factorial(2.5)

    def test_power_supports_zero_and_negative_exponents(self):
        self.assertEqual(power(3, 0), 1)
        self.assertEqual(power(2, 5), 32)
        self.assertEqual(power(2, -3), 0.125)

    def test_power_rejects_zero_to_negative_exponent(self):
        with self.assertRaises(ZeroDivisionError):
            power(0, -1)

    def test_sum_nested_handles_multiple_levels(self):
        self.assertEqual(sum_nested([1, (2, [3, 4]), 5]), 15)

    def test_sum_nested_rejects_non_numeric_values(self):
        with self.assertRaises(TypeError):
            sum_nested([1, ["two"]])


if __name__ == "__main__":
    unittest.main()
