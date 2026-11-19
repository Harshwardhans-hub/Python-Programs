"""Tests for directed DFS and undirected disjoint-set cycle detection."""

import unittest

from programs.graph_cycles import has_directed_cycle, has_undirected_cycle


class DirectedCycleTests(unittest.TestCase):
    def test_detects_back_edge_in_directed_graph(self):
        graph = {"a": ["b"], "b": ["c"], "c": ["a"]}
        self.assertTrue(has_directed_cycle(graph))

    def test_acyclic_graph_and_neighbor_only_nodes(self):
        graph = {"compile": ["package"], "lint": ["package"], "package": []}
        self.assertFalse(has_directed_cycle(graph))

    def test_detects_self_loop_and_handles_empty_graph(self):
        self.assertTrue(has_directed_cycle({"self": ["self"]}))
        self.assertFalse(has_directed_cycle({}))

    def test_long_chain_does_not_depend_on_python_recursion(self):
        graph = {index: [index + 1] for index in range(5000)}
        graph[5000] = []
        self.assertFalse(has_directed_cycle(graph))


class UndirectedCycleTests(unittest.TestCase):
    def test_tree_and_disconnected_forest_have_no_cycle(self):
        self.assertFalse(has_undirected_cycle([1, 2, 3, 4], [(1, 2), (2, 3)]))

    def test_detects_triangle_and_self_loop(self):
        self.assertTrue(has_undirected_cycle([1, 2, 3], [(1, 2), (2, 3), (3, 1)]))
        self.assertTrue(has_undirected_cycle([1], [(1, 1)]))

    def test_parallel_edges_count_as_a_cycle(self):
        self.assertTrue(has_undirected_cycle([1, 2], [(1, 2), (1, 2)]))

    def test_invalid_edge_shape_is_rejected(self):
        with self.assertRaises(ValueError):
            has_undirected_cycle([], [(1, 2, 3)])


if __name__ == "__main__":
    unittest.main()
