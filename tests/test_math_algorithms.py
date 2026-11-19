"""Tests for number-theory algorithms."""

import unittest

from programs.math_algorithms import modular_power, prime_factorization, sieve_primes


class MathAlgorithmTests(unittest.TestCase):
    def test_sieve_primes(self):
        self.assertEqual(sieve_primes(10), [2, 3, 5, 7])
        self.assertEqual(sieve_primes(1), [])

    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(360), {2: 3, 3: 2, 5: 1})
        self.assertEqual(prime_factorization(13), {13: 1})
        self.assertEqual(prime_factorization(1), {})

    def test_modular_power(self):
        self.assertEqual(modular_power(2, 10, 1000), 24)
        self.assertEqual(modular_power(5, 0, 7), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            prime_factorization(0)
        with self.assertRaises(ValueError):
            modular_power(2, -1, 7)
        with self.assertRaises(ValueError):
            modular_power(2, 3, 0)


if __name__ == "__main__":
    unittest.main()
