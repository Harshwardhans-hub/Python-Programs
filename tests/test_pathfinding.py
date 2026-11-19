"""Tests for shortest path search in blocked grids."""

import unittest

from programs.pathfinding import shortest_grid_path


class PathfindingTests(unittest.TestCase):
    def test_finds_shortest_path(self):
        grid = [
            [0, 0, 1],
            [1, 0, 0],
            [0, 0, 0],
        ]
        path = shortest_grid_path(grid, (0, 0), (2, 2))
        self.assertIsNotNone(path)
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (2, 2))
        self.assertEqual(len(path), 5)

    def test_blocked_or_unreachable_target_returns_none(self):
        self.assertIsNone(shortest_grid_path([[0, 1], [1, 0]], (0, 0), (1, 1)))
        self.assertIsNone(shortest_grid_path([[0, 1]], (0, 0), (0, 1)))

    def test_start_equal_target(self):
        self.assertEqual(shortest_grid_path([[0]], (0, 0), (0, 0)), [(0, 0)])

    def test_invalid_grid_and_coordinates_are_rejected(self):
        with self.assertRaises(ValueError):
            shortest_grid_path([], (0, 0), (0, 0))
        with self.assertRaises(IndexError):
            shortest_grid_path([[0]], (1, 0), (0, 0))
        with self.assertRaises(ValueError):
            shortest_grid_path([[2]], (0, 0), (0, 0))


    def test_single_row_corridor_returns_all_cells(self):
        self.assertEqual(
            shortest_grid_path([[0, 0, 0, 0]], (0, 0), (0, 3)),
            [(0, 0), (0, 1), (0, 2), (0, 3)],
        )

    def test_path_does_not_move_diagonally(self):
        self.assertIsNone(shortest_grid_path([[0, 1], [1, 0]], (0, 0), (1, 1)))



if __name__ == "__main__":
    unittest.main()
