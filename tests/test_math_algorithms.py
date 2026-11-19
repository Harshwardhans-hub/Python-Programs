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


    def test_prime_and_modular_helpers_cover_boundaries(self):
        self.assertEqual(sieve_primes(2), [2])
        self.assertEqual(sieve_primes(0), [])
        self.assertEqual(modular_power(-2, 5, 13), 7)
        self.assertEqual(modular_power(123, 5, 1), 0)

    def test_integer_only_arguments_reject_booleans_and_floats(self):
        with self.assertRaises(TypeError):
            sieve_primes(True)
        with self.assertRaises(TypeError):
            prime_factorization(2.0)
        with self.assertRaises(TypeError):
            modular_power(2, True, 7)



if __name__ == "__main__":
    unittest.main()
