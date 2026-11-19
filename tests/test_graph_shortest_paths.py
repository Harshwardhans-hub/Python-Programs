"""Tests for Dijkstra shortest path calculations."""

import unittest

from programs.graph_shortest_paths import dijkstra


class DijkstraTests(unittest.TestCase):
    def test_shortest_distances(self):
        graph = {
            "A": [("B", 4), ("C", 1)],
            "B": [("D", 1)],
            "C": [("B", 2), ("D", 5)],
            "D": [],
        }
        self.assertEqual(dijkstra(graph, "A"), {"A": 0, "B": 3, "C": 1, "D": 4})

    def test_unreachable_nodes_are_omitted(self):
        graph = {"A": [("B", 2)], "B": [], "isolated": []}
        self.assertEqual(dijkstra(graph, "A"), {"A": 0, "B": 2})

    def test_negative_edges_are_rejected(self):
        with self.assertRaises(ValueError):
            dijkstra({"A": [("B", -1)]}, "A")

    def test_non_numeric_edge_weight_is_rejected(self):
        with self.assertRaises(TypeError):
            dijkstra({"A": [("B", "heavy")]}, "A")


    def test_zero_weight_and_tied_paths_are_supported(self):
        graph = {
            "start": [("left", 1), (1, 1), ("free", 0)],
            "left": [("finish", 0)],
            1: [("finish", 0)],
            "free": [],
            "finish": [],
        }
        self.assertEqual(
            dijkstra(graph, "start"),
            {"start": 0, "left": 1, 1: 1, "free": 0, "finish": 1},
        )

    def test_unknown_start_is_a_valid_singleton_result(self):
        self.assertEqual(dijkstra({}, "outside"), {"outside": 0})



if __name__ == "__main__":
    unittest.main()
