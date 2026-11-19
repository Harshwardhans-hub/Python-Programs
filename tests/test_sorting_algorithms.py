"""Tests for bubble, insertion, selection, and quick sort."""

import unittest

from programs.sorting_algorithms import bubble_sort, insertion_sort, quick_sort, selection_sort


class SortingAlgorithmTests(unittest.TestCase):
    def test_all_sorts_order_numbers(self):
        values = [5, 1, 4, 1, 3, 9, 2]
        expected = [1, 1, 2, 3, 4, 5, 9]
        for sorter in (bubble_sort, insertion_sort, selection_sort, quick_sort):
            with self.subTest(sorter=sorter.__name__):
                self.assertEqual(sorter(values), expected)

    def test_sorts_do_not_mutate_input(self):
        values = [3, 1, 2]
        for sorter in (bubble_sort, insertion_sort, selection_sort, quick_sort):
            sorter(values)
            self.assertEqual(values, [3, 1, 2])

    def test_empty_single_and_string_inputs(self):
        for sorter in (bubble_sort, insertion_sort, selection_sort, quick_sort):
            self.assertEqual(sorter([]), [])
            self.assertEqual(sorter([1]), [1])
            self.assertEqual(sorter(["pear", "apple"]), ["apple", "pear"])


if __name__ == "__main__":
    unittest.main()
