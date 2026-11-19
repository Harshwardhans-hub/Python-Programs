"""Tests for Kruskal's minimum spanning forest."""

import unittest

from programs.minimum_spanning_forest import minimum_spanning_forest


class MinimumSpanningForestTests(unittest.TestCase):
    def test_selects_lowest_weight_edges_for_connected_graph(self):
        edges, total = minimum_spanning_forest(
            ["a", "b", "c", "d"],
            [("a", "b", 4), ("a", "c", 1), ("b", "c", 2), ("b", "d", 5), ("c", "d", 3)],
        )

        self.assertEqual(total, 6)
        self.assertEqual(len(edges), 3)
        self.assertEqual({weight for _a, _b, weight in edges}, {1, 2, 3})

    def test_disconnected_graph_returns_a_forest(self):
        edges, total = minimum_spanning_forest(
            [1, 2, 3, 4],
            [(1, 2, 7), (3, 4, 2)],
        )
        self.assertEqual(len(edges), 2)
        self.assertEqual(total, 9)

    def test_negative_weights_are_supported(self):
        edges, total = minimum_spanning_forest([1, 2], [(1, 2, -3)])
        self.assertEqual(edges, [(1, 2, -3)])
        self.assertEqual(total, -3)

    def test_invalid_edge_shapes_and_weights_are_rejected(self):
        with self.assertRaises(ValueError):
            minimum_spanning_forest([], [(1, 2)])
        with self.assertRaises(TypeError):
            minimum_spanning_forest([], [(1, 2, True)])


if __name__ == "__main__":
    unittest.main()
