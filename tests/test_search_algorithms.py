"""Tests for jump and exponential search."""

import unittest

from programs.search_algorithms import exponential_search, jump_search


class SearchAlgorithmTests(unittest.TestCase):
    def test_jump_search_finds_values_and_first_duplicate(self):
        values = [1, 3, 3, 5, 7, 9, 11]
        self.assertEqual(jump_search(values, 3), 1)
        self.assertEqual(jump_search(values, 11), 6)
        self.assertIsNone(jump_search(values, 4))

    def test_exponential_search_finds_values_and_first_duplicate(self):
        values = [1, 3, 3, 5, 7, 9, 11]
        self.assertEqual(exponential_search(values, 3), 1)
        self.assertEqual(exponential_search(values, 11), 6)
        self.assertIsNone(exponential_search(values, 12))

    def test_search_empty_and_single_item_sequences(self):
        for search in (jump_search, exponential_search):
            self.assertIsNone(search([], 1))
            self.assertEqual(search([5], 5), 0)
            self.assertIsNone(search([5], 4))


    def test_duplicate_run_crossing_search_blocks_returns_first_index(self):
        values = [0, 1, 2, 3, 7, 7, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        self.assertEqual(jump_search(values, 7), 4)
        self.assertEqual(exponential_search(values, 7), 4)



if __name__ == "__main__":
    unittest.main()
