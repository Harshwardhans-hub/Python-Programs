"""Tests for Fenwick tree point updates and range queries."""

import unittest

from programs.fenwick_tree import FenwickTree


class FenwickTreeTests(unittest.TestCase):
    def test_prefix_and_inclusive_range_queries(self):
        tree = FenwickTree([2, 4, 6, 8])
        self.assertEqual(tree.prefix_sum(-1), 0)
        self.assertEqual(tree.prefix_sum(2), 12)
        self.assertEqual(tree.range_sum(1, 3), 18)

    def test_point_update_changes_future_queries(self):
        tree = FenwickTree([1, 2, 3, 4])
        tree.add(1, 5)
        self.assertEqual(tree.range_sum(0, 3), 15)
        self.assertEqual(tree.range_sum(1, 2), 10)

    def test_empty_tree_supports_zero_prefix_only(self):
        tree = FenwickTree()
        self.assertEqual(len(tree), 0)
        self.assertEqual(tree.prefix_sum(-1), 0)
        with self.assertRaises(IndexError):
            tree.prefix_sum(0)

    def test_indexes_and_values_are_validated(self):
        tree = FenwickTree([1, 2])
        with self.assertRaises(IndexError):
            tree.add(2, 1)
        with self.assertRaises(TypeError):
            tree.add(True, 1)
        with self.assertRaises(TypeError):
            tree.add(0, False)
        with self.assertRaises(IndexError):
            tree.range_sum(1, 0)


if __name__ == "__main__":
    unittest.main()
