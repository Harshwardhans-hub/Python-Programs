"""Tests for the existing integer math helpers."""

import unittest

from programs.number_utils import (
    fibonacci_terms,
    greatest_common_divisor,
    is_prime,
    least_common_multiple,
)


class NumberUtilsTests(unittest.TestCase):
    def test_prime_checks_cover_small_and_composite_values(self):
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(99))

    def test_fibonacci_terms_returns_requested_count(self):
        self.assertEqual(fibonacci_terms(0), [])
        self.assertEqual(fibonacci_terms(1), [0])
        self.assertEqual(fibonacci_terms(7), [0, 1, 1, 2, 3, 5, 8])

    def test_fibonacci_terms_rejects_negative_and_non_integer_counts(self):
        with self.assertRaises(ValueError):
            fibonacci_terms(-1)
        with self.assertRaises(TypeError):
            fibonacci_terms(2.5)

    def test_gcd_and_lcm_handle_negative_and_zero_values(self):
        self.assertEqual(greatest_common_divisor(-54, 24), 6)
        self.assertEqual(least_common_multiple(12, 18), 36)
        self.assertEqual(least_common_multiple(0, 7), 0)

    def test_helpers_reject_boolean_and_non_integer_inputs(self):
        for helper, args in (
            (is_prime, (True,)),
            (greatest_common_divisor, (2, "4")),
            (least_common_multiple, (False, 4)),
        ):
            with self.subTest(helper=helper.__name__):
                with self.assertRaises(TypeError):
                    helper(*args)


if __name__ == "__main__":
    unittest.main()
