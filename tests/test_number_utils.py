"""Tests for integer math helpers."""

import unittest

from programs.number_utils import (
    greatest_common_divisor,
    is_prime,
    least_common_multiple,
    prime_factors,
)


class NumberUtilsTests(unittest.TestCase):
    def test_prime_checks_cover_small_and_composite_values(self):
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(97))
        self.assertFalse(is_prime(99))

    def test_prime_factors_preserve_multiplicity(self):
        self.assertEqual(prime_factors(360), [2, 2, 2, 3, 3, 5])
        self.assertEqual(prime_factors(-12), [2, 2, 3])
        self.assertEqual(prime_factors(1), [])

    def test_zero_has_no_finite_prime_factorization(self):
        with self.assertRaises(ValueError):
            prime_factors(0)

    def test_gcd_and_lcm_handle_negative_and_zero_values(self):
        self.assertEqual(greatest_common_divisor(-54, 24), 6)
        self.assertEqual(least_common_multiple(12, 18), 36)
        self.assertEqual(least_common_multiple(0, 7), 0)

    def test_helpers_reject_boolean_and_non_integer_inputs(self):
        for helper, args in (
            (is_prime, (True,)),
            (prime_factors, (2.5,)),
            (greatest_common_divisor, (2, "4")),
            (least_common_multiple, (False, 4)),
        ):
            with self.subTest(helper=helper.__name__):
                with self.assertRaises(TypeError):
                    helper(*args)


if __name__ == "__main__":
    unittest.main()
