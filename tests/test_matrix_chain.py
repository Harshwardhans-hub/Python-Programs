"""Tests for matrix-chain multiplication optimization."""

import unittest

from programs.matrix_chain import matrix_chain_order


class MatrixChainTests(unittest.TestCase):
    def test_classic_matrix_chain_example(self):
        cost, order = matrix_chain_order([30, 35, 15, 5, 10, 20, 25])

        self.assertEqual(cost, 15125)
        self.assertEqual(order, "((A1(A2A3))((A4A5)A6))")

    def test_two_matrices_need_one_multiplication(self):
        self.assertEqual(matrix_chain_order([10, 20, 30]), (6000, "(A1A2)"))

    def test_single_matrix_needs_no_multiplication(self):
        self.assertEqual(matrix_chain_order([7, 11]), (0, "A1"))

    def test_invalid_dimensions_are_rejected(self):
        for dimensions in ([], [10]):
            with self.subTest(dimensions=dimensions):
                with self.assertRaises(ValueError):
                    matrix_chain_order(dimensions)
        with self.assertRaises(ValueError):
            matrix_chain_order([10, 0, 20])
        with self.assertRaises(TypeError):
            matrix_chain_order([10, True, 20])
        with self.assertRaises(TypeError):
            matrix_chain_order("10,20")


if __name__ == "__main__":
    unittest.main()
