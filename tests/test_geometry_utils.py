"""Tests for two-dimensional geometry helpers."""

import unittest

from programs.geometry_utils import euclidean_distance, manhattan_distance, point_in_rectangle


class GeometryUtilsTests(unittest.TestCase):
    def test_distance_helpers(self):
        self.assertEqual(euclidean_distance((0, 0), (3, 4)), 5.0)
        self.assertEqual(manhattan_distance((0, 0), (3, 4)), 7)

    def test_rectangle_contains_inclusive_and_exclusive(self):
        bounds = ((0, 0), (4, 4))
        self.assertTrue(point_in_rectangle((0, 2), *bounds))
        self.assertFalse(point_in_rectangle((0, 2), *bounds, inclusive=False))
        self.assertTrue(point_in_rectangle((2, 2), *bounds, inclusive=False))

    def test_rectangle_validation(self):
        with self.assertRaises(ValueError):
            point_in_rectangle((1, 1), (5, 5), (0, 0))
        with self.assertRaises(TypeError):
            euclidean_distance(("x", 0), (0, 0))


    def test_zero_distance_and_degenerate_rectangle(self):
        self.assertEqual(euclidean_distance((2, 2), (2, 2)), 0.0)
        self.assertEqual(manhattan_distance((2, 2), (2, 2)), 0)
        self.assertTrue(point_in_rectangle((2, 2), (2, 2), (2, 2)))
        self.assertFalse(point_in_rectangle((2, 2), (2, 2), (2, 2), inclusive=False))

    def test_coordinate_validation_rejects_booleans_and_wrong_dimensions(self):
        with self.assertRaises(TypeError):
            euclidean_distance((True, 0), (0, 0))
        with self.assertRaises(ValueError):
            manhattan_distance((0, 1, 2), (0, 0))



if __name__ == "__main__":
    unittest.main()
