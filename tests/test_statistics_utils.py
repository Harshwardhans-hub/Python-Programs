"""Tests for descriptive statistics helpers."""

import math
import unittest

from programs.statistics_utils import mean, median, population_std_dev, population_variance


class StatisticsUtilsTests(unittest.TestCase):
    def test_mean(self):
        self.assertEqual(mean([2, 4, 6]), 4.0)

    def test_median_for_odd_and_even_lengths(self):
        self.assertEqual(median([9, 1, 5]), 5.0)
        self.assertEqual(median([1, 2, 8, 9]), 5.0)

    def test_population_variance_and_standard_deviation(self):
        self.assertEqual(population_variance([2, 4, 4, 4, 5, 5, 7, 9]), 4.0)
        self.assertEqual(population_std_dev([2, 4, 4, 4, 5, 5, 7, 9]), 2.0)

    def test_single_value_has_zero_spread(self):
        self.assertEqual(population_variance([12]), 0.0)
        self.assertEqual(population_std_dev([12]), 0.0)

    def test_empty_input_is_rejected(self):
        for function in (mean, median, population_variance, population_std_dev):
            with self.subTest(function=function.__name__):
                with self.assertRaises(ValueError):
                    function([])

    def test_non_numeric_and_non_finite_values_are_rejected(self):
        with self.assertRaises(TypeError):
            mean([1, "two"])
        with self.assertRaises(ValueError):
            median([1, math.inf])


if __name__ == "__main__":
    unittest.main()
