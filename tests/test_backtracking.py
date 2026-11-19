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


    def test_empty_subset_input_has_one_empty_subset(self):
        self.assertEqual(subsets([]), [[]])

    def test_five_queens_solutions_have_no_column_or_diagonal_conflicts(self):
        solutions = solve_n_queens(5)
        self.assertEqual(len(solutions), 10)
        for placement in solutions:
            self.assertEqual(len(set(placement)), 5)
            diagonals = [row - col for row, col in enumerate(placement)]
            anti_diagonals = [row + col for row, col in enumerate(placement)]
            self.assertEqual(len(set(diagonals)), 5)
            self.assertEqual(len(set(anti_diagonals)), 5)



if __name__ == "__main__":
    unittest.main()
