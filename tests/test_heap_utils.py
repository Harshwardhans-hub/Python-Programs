"""Tests for heap-backed selection and merge helpers."""

import unittest

from programs.heap_utils import kth_smallest, merge_sorted_sequences, top_k_largest


class HeapUtilsTests(unittest.TestCase):
    def test_top_k_largest(self):
        self.assertEqual(top_k_largest([3, 1, 8, 5, 2], 3), [8, 5, 3])
        self.assertEqual(top_k_largest([1, 2], 0), [])

    def test_top_k_rejects_invalid_count(self):
        with self.assertRaises(ValueError):
            top_k_largest([1], -1)
        with self.assertRaises(TypeError):
            top_k_largest([1], True)

    def test_kth_smallest_is_one_based(self):
        self.assertEqual(kth_smallest([8, 2, 5, 1], 3), 5)

    def test_kth_smallest_rejects_out_of_range_rank(self):
        with self.assertRaises(ValueError):
            kth_smallest([1, 2], 0)
        with self.assertRaises(IndexError):
            kth_smallest([1, 2], 3)

    def test_merge_sorted_sequences(self):
        self.assertEqual(merge_sorted_sequences([1, 4], [2, 3], [], [5]), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
