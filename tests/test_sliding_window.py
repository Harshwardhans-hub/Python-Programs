"""Tests for sliding window and prefix-sum helpers."""

import unittest

from programs.sliding_window import (
    count_subarrays_with_sum,
    longest_unique_substring_length,
    maximum_subarray_sum,
)


class SlidingWindowTests(unittest.TestCase):
    def test_maximum_fixed_window_sum(self):
        self.assertEqual(maximum_subarray_sum([2, 1, 5, 1, 3, 2], 3), 9)
        self.assertEqual(maximum_subarray_sum([-5, -2, -7], 2), -7)

    def test_maximum_window_handles_oversized_and_invalid_windows(self):
        self.assertIsNone(maximum_subarray_sum([1, 2], 3))
        with self.assertRaises(ValueError):
            maximum_subarray_sum([1, 2], 0)
        with self.assertRaises(TypeError):
            maximum_subarray_sum([1, 2], True)

    def test_longest_unique_substring(self):
        self.assertEqual(longest_unique_substring_length("abcabcbb"), 3)
        self.assertEqual(longest_unique_substring_length("bbbbb"), 1)
        self.assertEqual(longest_unique_substring_length(""), 0)

    def test_count_subarrays_with_sum_supports_negative_values(self):
        self.assertEqual(count_subarrays_with_sum([1, 1, 1], 2), 2)
        self.assertEqual(count_subarrays_with_sum([1, -1, 0], 0), 3)


if __name__ == "__main__":
    unittest.main()
