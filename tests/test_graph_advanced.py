"""Tests for advanced graph algorithms."""

import unittest

from programs.graph_advanced import shortest_unweighted_path, topological_sort


class AdvancedGraphTests(unittest.TestCase):
    def test_topological_sort_respects_dependencies(self):
        graph = {"build": ["test"], "lint": ["test"], "test": ["release"], "release": []}
        result = topological_sort(graph)
        positions = {node: index for index, node in enumerate(result)}
        self.assertLess(positions["build"], positions["test"])
        self.assertLess(positions["lint"], positions["test"])
        self.assertLess(positions["test"], positions["release"])

    def test_topological_sort_rejects_cycles(self):
        with self.assertRaises(ValueError):
            topological_sort({"a": ["b"], "b": ["a"]})

    def test_shortest_unweighted_path(self):
        graph = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}
        self.assertEqual(shortest_unweighted_path(graph, "A", "D"), ["A", "B", "D"])

    def test_shortest_path_handles_same_and_unreachable_nodes(self):
        self.assertEqual(shortest_unweighted_path({}, "A", "A"), ["A"])
        self.assertIsNone(shortest_unweighted_path({"A": []}, "A", "B"))


if __name__ == "__main__":
    unittest.main()
