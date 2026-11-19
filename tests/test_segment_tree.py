"""Tests for iterative segment tree behavior."""

import unittest

from programs.segment_tree import SegmentTree


class SegmentTreeTests(unittest.TestCase):
    def test_range_sum_matches_expected_inclusive_ranges(self):
        tree = SegmentTree([3, 1, 4, 1, 5, 9])
        self.assertEqual(tree.range_sum(0, 5), 23)
        self.assertEqual(tree.range_sum(2, 4), 10)
        self.assertEqual(tree.range_sum(3, 3), 1)

    def test_point_update_recalculates_parent_sums(self):
        tree = SegmentTree([1, 2, 3, 4])
        tree.update(2, 10)
        self.assertEqual(tree.range_sum(0, 3), 17)
        self.assertEqual(tree.range_sum(2, 3), 14)

    def test_non_power_of_two_lengths_are_supported(self):
        tree = SegmentTree([5, 6, 7])
        self.assertEqual(tree.range_sum(0, 2), 18)

    def test_empty_and_invalid_indexes(self):
        tree = SegmentTree()
        self.assertEqual(len(tree), 0)
        with self.assertRaises(IndexError):
            tree.range_sum(0, 0)
        with self.assertRaises(TypeError):
            SegmentTree([True])


    def test_repeated_replacements_match_naive_list_sums(self):
        values = [4, -1, 8, 2, 0, 5, 3]
        tree = SegmentTree(values)
        replacements = [(0, 10), (3, -4), (6, 9), (2, 1)]
        for index, value in replacements:
            values[index] = value
            tree.update(index, value)
            for start in range(len(values)):
                for end in range(start, len(values)):
                    self.assertEqual(tree.range_sum(start, end), sum(values[start:end + 1]))



if __name__ == "__main__":
    unittest.main()
