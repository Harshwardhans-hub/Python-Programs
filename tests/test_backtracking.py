"""Tests for subset, permutation, and N-Queens backtracking examples."""

import unittest

from programs.backtracking import permutations, solve_n_queens, subsets


class BacktrackingTests(unittest.TestCase):
    def test_subsets_include_empty_and_full_sets(self):
        result = subsets([1, 2])
        self.assertEqual(len(result), 4)
        self.assertIn([], result)
        self.assertIn([1, 2], result)

    def test_subsets_preserve_positional_duplicates(self):
        self.assertEqual(len(subsets([1, 1])), 4)

    def test_permutations(self):
        result = permutations([1, 2, 3])
        self.assertEqual(len(result), 6)
        self.assertIn([3, 2, 1], result)

    def test_empty_permutation_has_one_empty_result(self):
        self.assertEqual(permutations([]), [[]])

    def test_n_queens_known_solution_counts(self):
        self.assertEqual(len(solve_n_queens(1)), 1)
        self.assertEqual(len(solve_n_queens(2)), 0)
        self.assertEqual(len(solve_n_queens(4)), 2)

    def test_n_queens_rejects_invalid_board_size(self):
        with self.assertRaises(ValueError):
            solve_n_queens(0)
        with self.assertRaises(TypeError):
            solve_n_queens(2.5)


if __name__ == "__main__":
    unittest.main()
