"""Tests for graph traversal and path search."""

import unittest

from programs.graph_algorithms import breadth_first_search, depth_first_search, has_path


class GraphAlgorithmTests(unittest.TestCase):
    def setUp(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["E"],
            "D": [],
            "E": ["B"],
            "isolated": [],
        }

    def test_breadth_first_search_order(self):
        self.assertEqual(breadth_first_search(self.graph, "A"), ["A", "B", "C", "D", "E"])

    def test_depth_first_search_order(self):
        self.assertEqual(depth_first_search(self.graph, "A"), ["A", "B", "D", "C", "E"])

    def test_traversal_handles_unknown_start_node(self):
        self.assertEqual(breadth_first_search(self.graph, "missing"), ["missing"])
        self.assertEqual(depth_first_search(self.graph, "missing"), ["missing"])

    def test_traversals_handle_cycles(self):
        self.assertEqual(len(breadth_first_search(self.graph, "A")), 5)
        self.assertEqual(len(depth_first_search(self.graph, "A")), 5)

    def test_has_path(self):
        self.assertTrue(has_path(self.graph, "A", "E"))
        self.assertFalse(has_path(self.graph, "A", "isolated"))
        self.assertTrue(has_path(self.graph, "A", "A"))


if __name__ == "__main__":
    unittest.main()
