"""Tests for combinatorics helpers."""

import unittest

from programs.combinatorics_utils import binomial_coefficient, combinations, pascal_triangle


class CombinatoricsUtilsTests(unittest.TestCase):
    def test_pascal_triangle_rows(self):
        self.assertEqual(pascal_triangle(5), [
            [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]
        ])
        self.assertEqual(pascal_triangle(0), [])

    def test_binomial_coefficient(self):
        self.assertEqual(binomial_coefficient(5, 2), 10)
        self.assertEqual(binomial_coefficient(4, 0), 1)
        self.assertEqual(binomial_coefficient(3, 5), 0)

    def test_combinations(self):
        self.assertEqual(combinations(["a", "b", "c"], 2), [["a", "b"], ["a", "c"], ["b", "c"]])
        self.assertEqual(combinations([1, 2], 0), [[]])
        self.assertEqual(combinations([1], 2), [])

    def test_invalid_counts_are_rejected(self):
        with self.assertRaises(ValueError):
            pascal_triangle(-1)
        with self.assertRaises(TypeError):
            binomial_coefficient(True, 1)
        with self.assertRaises(ValueError):
            combinations([1], -1)


if __name__ == "__main__":
    unittest.main()
