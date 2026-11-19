"""Tests for rectangular-grid traversal helpers."""

import unittest

from programs.grid_algorithms import count_islands, flood_fill


class GridAlgorithmTests(unittest.TestCase):
    def test_flood_fill_recolors_connected_region(self):
        grid = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        self.assertEqual(flood_fill(grid, 1, 1, 2), [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
        self.assertEqual(grid, [[1, 1, 1], [1, 1, 0], [1, 0, 1]])

    def test_flood_fill_same_color_returns_copy(self):
        grid = [[1, 1]]
        result = flood_fill(grid, 0, 0, 1)
        self.assertEqual(result, grid)
        self.assertIsNot(result, grid)

    def test_flood_fill_rejects_out_of_bounds_start(self):
        with self.assertRaises(IndexError):
            flood_fill([[1]], 1, 0, 2)

    def test_count_islands(self):
        grid = [
            [1, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 1],
        ]
        self.assertEqual(count_islands(grid), 2)

    def test_count_islands_validates_cells_and_rectangular_shape(self):
        with self.assertRaises(ValueError):
            count_islands([[1, 2]])
        with self.assertRaises(ValueError):
            count_islands([[1, 0], [1]])


if __name__ == "__main__":
    unittest.main()
