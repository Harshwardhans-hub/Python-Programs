"""Tests for constant-time prefix-sum range queries."""

import unittest

from programs.prefix_sums import PrefixSum


class PrefixSumTests(unittest.TestCase):
    def test_inclusive_range_sum(self):
        values = PrefixSum([2, 4, 6, 8])
        self.assertEqual(values.range_sum(0, 3), 20)
        self.assertEqual(values.range_sum(1, 2), 10)
        self.assertEqual(values.range_sum(2, 2), 6)

    def test_empty_sequence_length(self):
        self.assertEqual(len(PrefixSum([])), 0)

    def test_invalid_ranges_are_rejected(self):
        values = PrefixSum([1, 2, 3])
        with self.assertRaises(IndexError):
            values.range_sum(-1, 1)
        with self.assertRaises(IndexError):
            values.range_sum(2, 1)
        with self.assertRaises(IndexError):
            values.range_sum(0, 3)

    def test_non_numeric_values_are_rejected(self):
        with self.assertRaises(TypeError):
            PrefixSum([1, "two"])


if __name__ == "__main__":
    unittest.main()
