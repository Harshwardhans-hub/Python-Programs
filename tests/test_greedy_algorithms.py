"""Tests for greedy algorithm examples."""

import unittest

from programs.greedy_algorithms import fractional_knapsack, select_activities


class GreedyAlgorithmTests(unittest.TestCase):
    def test_activity_selection_returns_maximum_compatible_set(self):
        starts = [1, 3, 0, 5, 8, 5]
        ends = [2, 4, 6, 7, 9, 9]
        chosen = select_activities(starts, ends)
        self.assertEqual(chosen, [0, 1, 3, 4])

    def test_activity_selection_handles_empty_and_invalid_inputs(self):
        self.assertEqual(select_activities([], []), [])
        with self.assertRaises(ValueError):
            select_activities([1], [])
        with self.assertRaises(ValueError):
            select_activities([4], [2])

    def test_fractional_knapsack(self):
        self.assertAlmostEqual(
            fractional_knapsack([10, 20, 30], [60, 100, 120], 50),
            240.0,
        )

    def test_fractional_knapsack_rejects_invalid_inputs(self):
        with self.assertRaises(ValueError):
            fractional_knapsack([0], [10], 5)
        with self.assertRaises(ValueError):
            fractional_knapsack([1], [10], -1)
        with self.assertRaises(ValueError):
            fractional_knapsack([1], [10, 20], 5)


    def test_half_open_activity_intervals_allow_back_to_back_starts(self):
        self.assertEqual(
            select_activities([1, 2, 2], [2, 3, 4]),
            [0, 1],
        )

    def test_fractional_knapsack_zero_capacity_returns_zero(self):
        self.assertEqual(fractional_knapsack([2, 3], [4, 5], 0), 0.0)



if __name__ == "__main__":
    unittest.main()
