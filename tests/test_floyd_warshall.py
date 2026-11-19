"""Tests for all-pairs shortest path distances."""

import math
import unittest

from programs.floyd_warshall import floyd_warshall


class FloydWarshallTests(unittest.TestCase):
    def test_calculates_shortest_paths_through_intermediate_nodes(self):
        graph = {
            "a": [("b", 3), ("c", 10)],
            "b": [("c", 2)],
            "c": [],
        }
        result = floyd_warshall(graph)

        self.assertEqual(result["a"]["c"], 5)
        self.assertEqual(result["a"]["b"], 3)
        self.assertEqual(result["c"]["c"], 0)

    def test_supports_negative_edges_without_negative_cycles(self):
        result = floyd_warshall({
            "a": [("b", 4)],
            "b": [("c", -6)],
            "c": [("d", 3)],
            "d": [],
        })
        self.assertEqual(result["a"]["c"], -2)
        self.assertEqual(result["a"]["d"], 1)

    def test_unreachable_pairs_are_infinite(self):
        result = floyd_warshall({"a": [], "b": [("c", 1)], "c": []})
        self.assertTrue(math.isinf(result["a"]["b"]))
        self.assertEqual(result["b"]["c"], 1)

    def test_negative_cycle_is_rejected(self):
        with self.assertRaises(ValueError):
            floyd_warshall({"a": [("b", 1)], "b": [("a", -2)]})

    def test_invalid_edge_weight_is_rejected(self):
        with self.assertRaises(TypeError):
            floyd_warshall({"a": [("b", True)]})


if __name__ == "__main__":
    unittest.main()
