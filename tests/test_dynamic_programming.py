"""Tests for coin change, LIS, and 0/1 knapsack exercises."""

import unittest

from programs.dynamic_programming import (
    longest_increasing_subsequence_length,
    minimum_coin_change,
    zero_one_knapsack,
)


class DynamicProgrammingTests(unittest.TestCase):
    def test_minimum_coin_change(self):
        self.assertEqual(minimum_coin_change([1, 2, 5], 11), 3)
        self.assertEqual(minimum_coin_change([2], 3), None)
        self.assertEqual(minimum_coin_change([2, 5], 0), 0)

    def test_coin_change_rejects_invalid_amount_and_coins(self):
        with self.assertRaises(ValueError):
            minimum_coin_change([1, 2], -1)
        with self.assertRaises(ValueError):
            minimum_coin_change([0, 2], 4)
        with self.assertRaises(TypeError):
            minimum_coin_change([1, 2.5], 4)

    def test_lis_handles_duplicates_and_empty_sequences(self):
        self.assertEqual(longest_increasing_subsequence_length([10, 9, 2, 5, 3, 7, 101, 18]), 4)
        self.assertEqual(longest_increasing_subsequence_length([2, 2, 2]), 1)
        self.assertEqual(longest_increasing_subsequence_length([]), 0)

    def test_zero_one_knapsack(self):
        self.assertEqual(zero_one_knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5), 7)
        self.assertEqual(zero_one_knapsack([], [], 0), 0)

    def test_knapsack_rejects_mismatched_arrays_and_negative_capacity(self):
        with self.assertRaises(ValueError):
            zero_one_knapsack([1], [1, 2], 4)
        with self.assertRaises(ValueError):
            zero_one_knapsack([1], [1], -1)


    def test_knapsack_supports_zero_weight_items_once(self):
        self.assertEqual(zero_one_knapsack([0, 2], [4, 3], 2), 7)

    def test_coin_change_with_empty_denominations(self):
        self.assertEqual(minimum_coin_change([], 0), 0)
        self.assertIsNone(minimum_coin_change([], 5))



if __name__ == "__main__":
    unittest.main()
