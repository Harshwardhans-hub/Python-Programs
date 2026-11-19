"""Tests for breadth-first bipartite graph checking."""

import unittest

from programs.bipartite import is_bipartite


class BipartiteTests(unittest.TestCase):
    def test_even_cycle_is_bipartite(self):
        graph = {1: [2, 4], 2: [1, 3], 3: [2, 4], 4: [1, 3]}
        self.assertTrue(is_bipartite(graph))

    def test_odd_cycle_is_not_bipartite(self):
        graph = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
        self.assertFalse(is_bipartite(graph))

    def test_disconnected_graph_with_isolated_vertices(self):
        self.assertTrue(is_bipartite({1: [2], 3: [4], 5: []}))

    def test_self_loop_is_not_bipartite(self):
        self.assertFalse(is_bipartite({"loop": ["loop"]}))

    def test_one_sided_adjacency_is_treated_as_undirected(self):
        self.assertTrue(is_bipartite({"a": ["b"], "b": ["c"], "c": []}))
        self.assertFalse(is_bipartite({"a": ["b"], "b": ["c"], "c": ["a"]}))


if __name__ == "__main__":
    unittest.main()
