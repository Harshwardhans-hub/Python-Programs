"""Tests for Armstrong, perfect-number, leap-year, and digit-sum helpers."""

import unittest

from programs.number_theory import is_armstrong_number, is_leap_year, is_perfect_number, sum_of_digits


class NumberTheoryTests(unittest.TestCase):
    def test_armstrong_numbers(self):
        for number in (0, 1, 153, 370, 371, 407, 9474):
            with self.subTest(number=number):
                self.assertTrue(is_armstrong_number(number))
        self.assertFalse(is_armstrong_number(154))
        self.assertFalse(is_armstrong_number(-153))

    def test_perfect_numbers(self):
        for number in (6, 28, 496, 8128):
            with self.subTest(number=number):
                self.assertTrue(is_perfect_number(number))
        self.assertFalse(is_perfect_number(1))
        self.assertFalse(is_perfect_number(12))

    def test_gregorian_leap_year_rules(self):
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1900))
        self.assertTrue(is_leap_year(2024))
        self.assertFalse(is_leap_year(2023))

    def test_sum_of_digits_handles_negative_numbers(self):
        self.assertEqual(sum_of_digits(5021), 8)
        self.assertEqual(sum_of_digits(-5021), 8)

    def test_helpers_reject_booleans(self):
        with self.assertRaises(TypeError):
            is_leap_year(True)
        with self.assertRaises(TypeError):
            sum_of_digits(False)


if __name__ == "__main__":
    unittest.main()
