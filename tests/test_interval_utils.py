"""Tests for closed interval normalization helpers."""

import unittest

from programs.interval_utils import insert_interval, merge_intervals


class IntervalUtilsTests(unittest.TestCase):
    def test_merge_overlapping_and_touching_intervals(self):
        self.assertEqual(merge_intervals([(1, 3), (2, 5), (5, 7), (10, 12)]),
                         [(1, 7), (10, 12)])

    def test_can_keep_touching_intervals_separate(self):
        self.assertEqual(merge_intervals([(1, 2), (2, 3)], merge_touching=False),
                         [(1, 2), (2, 3)])

    def test_merge_sorts_input_without_mutating_it(self):
        original = [(8, 9), (1, 2), (3, 4)]
        self.assertEqual(merge_intervals(original), [(1, 2), (3, 4), (8, 9)])
        self.assertEqual(original, [(8, 9), (1, 2), (3, 4)])

    def test_insert_interval(self):
        self.assertEqual(insert_interval([(1, 2), (6, 9)], (2, 7)), [(1, 9)])

    def test_invalid_interval_is_rejected(self):
        with self.assertRaises(ValueError):
            merge_intervals([(3, 1)])
        with self.assertRaises(ValueError):
            merge_intervals([(1, 2, 3)])


    def test_empty_and_zero_length_intervals(self):
        self.assertEqual(merge_intervals([]), [])
        self.assertEqual(merge_intervals([(2, 2), (2, 2), (-1, -1)]), [(-1, -1), (2, 2)])

    def test_insert_does_not_mutate_original_intervals(self):
        original = [(5, 7), (1, 2)]
        snapshot = original.copy()
        self.assertEqual(insert_interval(original, (2, 5)), [(1, 7)])
        self.assertEqual(original, snapshot)



if __name__ == "__main__":
    unittest.main()
