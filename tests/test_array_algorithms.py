"""Tests for maximum subarray, product-except-self, and zero movement."""

import unittest

from programs.array_algorithms import maximum_subarray_sum, move_zeros_to_end, product_except_self


class ArrayAlgorithmTests(unittest.TestCase):
    def test_maximum_subarray_sum(self):
        self.assertEqual(maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)
        self.assertEqual(maximum_subarray_sum([-8, -3, -6]), -3)
        self.assertIsNone(maximum_subarray_sum([]))

    def test_product_except_self_with_zeros(self):
        self.assertEqual(product_except_self([1, 2, 3, 4]), [24, 12, 8, 6])
        self.assertEqual(product_except_self([1, 2, 0, 4]), [0, 0, 8, 0])
        self.assertEqual(product_except_self([]), [])

    def test_move_zeros_preserves_non_zero_order(self):
        self.assertEqual(move_zeros_to_end([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
        self.assertEqual(move_zeros_to_end([0, 0]), [0, 0])

    def test_maximum_subarray_validates_values(self):
        with self.assertRaises(TypeError):
            maximum_subarray_sum([1, "bad"])


    def test_single_item_and_all_zero_product_cases(self):
        self.assertEqual(product_except_self([9]), [1])
        self.assertEqual(product_except_self([0, 0, 5]), [0, 0, 0])
        self.assertEqual(move_zeros_to_end([]), [])



if __name__ == "__main__":
    unittest.main()
