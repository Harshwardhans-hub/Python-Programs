"""Tests for the searching and sorting exercises."""

import unittest

from programs.algorithms import binary_search, linear_search, merge_sort


class SearchingTests(unittest.TestCase):
    def test_linear_search_returns_first_match(self):
        self.assertEqual(linear_search(["a", "b", "b"], "b"), 1)

    def test_linear_search_returns_none_when_missing(self):
        self.assertIsNone(linear_search([1, 3, 5], 2))

    def test_binary_search_handles_empty_and_missing_values(self):
        self.assertIsNone(binary_search([], 10))
        self.assertIsNone(binary_search([1, 3, 5], 2))

    def test_binary_search_returns_first_duplicate(self):
        self.assertEqual(binary_search([1, 2, 2, 2, 4], 2), 1)


class SortingTests(unittest.TestCase):
    def test_merge_sort_sorts_without_mutating_input(self):
        original = [5, 1, 4, 1, 3]
        self.assertEqual(merge_sort(original), [1, 1, 3, 4, 5])
        self.assertEqual(original, [5, 1, 4, 1, 3])

    def test_merge_sort_handles_empty_and_single_item_sequences(self):
        self.assertEqual(merge_sort([]), [])
        self.assertEqual(merge_sort([7]), [7])

    def test_merge_sort_supports_strings(self):
        self.assertEqual(merge_sort(["pear", "apple", "orange"]), ["apple", "orange", "pear"])


if __name__ == "__main__":
    unittest.main()
