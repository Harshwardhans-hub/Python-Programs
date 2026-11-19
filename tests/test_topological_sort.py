"""Tests for Kahn topological sorting."""

import unittest

from programs.topological_sort import topological_sort


class TopologicalSortTests(unittest.TestCase):
    def test_orders_dependency_graph(self):
        graph = {"parse": ["compile"], "lint": ["compile"], "compile": ["package"], "package": []}
        order = topological_sort(graph)
        positions = {node: index for index, node in enumerate(order)}

        self.assertEqual(set(order), {"parse", "lint", "compile", "package"})
        self.assertLess(positions["parse"], positions["compile"])
        self.assertLess(positions["lint"], positions["compile"])
        self.assertLess(positions["compile"], positions["package"])

    def test_includes_neighbor_only_and_isolated_nodes(self):
        self.assertEqual(topological_sort({"root": ["leaf"], "alone": []}), ["root", "alone", "leaf"])

    def test_empty_graph_returns_empty_order(self):
        self.assertEqual(topological_sort({}), [])

    def test_cycle_is_rejected(self):
        with self.assertRaises(ValueError):
            topological_sort({"a": ["b"], "b": ["c"], "c": ["a"]})


    def test_returned_order_respects_every_edge_with_repeated_dependencies(self):
        graph = {"a": ["c", "c"], "b": ["c"], "c": ["d"], "d": []}
        order = topological_sort(graph)
        positions = {node: index for index, node in enumerate(order)}
        for source, neighbors in graph.items():
            for target in neighbors:
                self.assertLess(positions[source], positions[target])



if __name__ == "__main__":
    unittest.main()
