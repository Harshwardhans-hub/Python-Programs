"""Tests for Bellman-Ford shortest paths."""

import unittest

from programs.bellman_ford import bellman_ford


class BellmanFordTests(unittest.TestCase):
    def test_finds_shortest_paths_with_negative_edges(self):
        graph = {
            "s": [("a", 4), ("b", 5)],
            "a": [("b", -2), ("t", 4)],
            "b": [("t", 3)],
            "t": [],
        }
        self.assertEqual(bellman_ford(graph, "s"), {"s": 0, "a": 4, "b": 2, "t": 5})

    def test_unreachable_nodes_are_omitted(self):
        self.assertEqual(
            bellman_ford({"s": [("a", 2)], "a": [], "isolated": []}, "s"),
            {"s": 0, "a": 2},
        )

    def test_reachable_negative_cycle_is_rejected(self):
        graph = {"s": [("a", 1)], "a": [("b", -2)], "b": [("a", -2)]}
        with self.assertRaises(ValueError):
            bellman_ford(graph, "s")

    def test_negative_cycle_in_unreachable_component_is_ignored(self):
        graph = {"s": [], "x": [("y", -2)], "y": [("x", -2)]}
        self.assertEqual(bellman_ford(graph, "s"), {"s": 0})

    def test_bad_weights_are_rejected(self):
        with self.assertRaises(TypeError):
            bellman_ford({"s": [("t", True)]}, "s")


    def test_non_negative_graph_matches_dijkstra(self):
        from programs.graph_shortest_paths import dijkstra

        graph = {
            "s": [("a", 4), ("b", 5)],
            "a": [("b", 2), ("t", 4)],
            "b": [("t", 3)],
            "t": [],
        }
        self.assertEqual(bellman_ford(graph, "s"), dijkstra(graph, "s"))



if __name__ == "__main__":
    unittest.main()
