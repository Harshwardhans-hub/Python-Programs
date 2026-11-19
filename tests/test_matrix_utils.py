"""Tests for matrix transpose, addition, multiplication, and rotation."""

import unittest

from programs.matrix_utils import add_matrices, multiply_matrices, rotate_clockwise, transpose


class MatrixUtilsTests(unittest.TestCase):
    def test_transpose(self):
        self.assertEqual(transpose([[1, 2, 3], [4, 5, 6]]), [[1, 4], [2, 5], [3, 6]])

    def test_transpose_empty_matrix(self):
        self.assertEqual(transpose([]), [])

    def test_add_matrices(self):
        self.assertEqual(add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]), [[6, 8], [10, 12]])

    def test_add_rejects_different_shapes(self):
        with self.assertRaises(ValueError):
            add_matrices([[1, 2]], [[1], [2]])

    def test_multiply_matrices(self):
        self.assertEqual(multiply_matrices([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]),
                         [[58, 64], [139, 154]])

    def test_multiply_rejects_incompatible_dimensions(self):
        with self.assertRaises(ValueError):
            multiply_matrices([[1, 2]], [[1, 2]])

    def test_rotation_supports_rectangular_matrices(self):
        self.assertEqual(rotate_clockwise([[1, 2, 3], [4, 5, 6]]), [[4, 1], [5, 2], [6, 3]])

    def test_ragged_rows_are_rejected(self):
        with self.assertRaises(ValueError):
            transpose([[1, 2], [3]])


    def test_operations_do_not_mutate_input_matrices(self):
        first = [[1, 2], [3, 4]]
        second = [[5, 6], [7, 8]]
        first_before, second_before = [row[:] for row in first], [row[:] for row in second]

        add_matrices(first, second)
        multiply_matrices(first, second)
        transpose(first)
        rotate_clockwise(first)

        self.assertEqual(first, first_before)
        self.assertEqual(second, second_before)

    def test_boolean_matrix_values_are_rejected(self):
        with self.assertRaises(TypeError):
            transpose([[True, 0]])



if __name__ == "__main__":
    unittest.main()
