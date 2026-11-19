"""Tests for deque-based 0-1 BFS."""

import unittest

from programs.zero_one_bfs import zero_one_bfs


class ZeroOneBFSTests(unittest.TestCase):
    def test_prefers_zero_weight_routes_over_more_expensive_routes(self):
        graph = {
            "start": [("a", 1), ("b", 0)],
            "a": [("end", 0)],
            "b": [("a", 0), ("end", 1)],
            "end": [],
        }
        self.assertEqual(zero_one_bfs(graph, "start"), {
            "start": 0, "a": 0, "b": 0, "end": 0
        })

    def test_unreachable_nodes_are_omitted(self):
        self.assertEqual(zero_one_bfs({"a": [("b", 1)], "b": [], "x": []}, "a"),
                         {"a": 0, "b": 1})

    def test_unknown_start_is_included(self):
        self.assertEqual(zero_one_bfs({}, "new"), {"new": 0})

    def test_invalid_weights_and_edge_shapes_are_rejected(self):
        with self.assertRaises(ValueError):
            zero_one_bfs({"a": [("b", 2)]}, "a")
        with self.assertRaises(ValueError):
            zero_one_bfs({"a": [("b", 0, "extra")]}, "a")
        with self.assertRaises(TypeError):
            zero_one_bfs({"a": [("b", True)]}, "a")


if __name__ == "__main__":
    unittest.main()
