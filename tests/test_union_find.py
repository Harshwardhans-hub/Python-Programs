"""Tests for disjoint-set union-find."""

import unittest

from programs.union_find import DisjointSet


class DisjointSetTests(unittest.TestCase):
    def test_initial_components_and_add(self):
        sets = DisjointSet(["a", "b", "c"])
        self.assertEqual(sets.component_count, 3)
        sets.add("d")
        self.assertEqual(sets.component_count, 4)
        sets.add("d")
        self.assertEqual(sets.component_count, 4)

    def test_union_merges_components_once(self):
        sets = DisjointSet([1, 2, 3])
        self.assertTrue(sets.union(1, 2))
        self.assertFalse(sets.union(2, 1))
        self.assertEqual(sets.component_count, 2)
        self.assertTrue(sets.connected(1, 2))
        self.assertFalse(sets.connected(1, 3))

    def test_find_adds_unknown_values(self):
        sets = DisjointSet()
        self.assertEqual(sets.find("new"), "new")
        self.assertEqual(sets.component_count, 1)

    def test_transitive_connectivity(self):
        sets = DisjointSet([1, 2, 3, 4])
        sets.union(1, 2)
        sets.union(3, 4)
        sets.union(2, 3)
        self.assertTrue(sets.connected(1, 4))
        self.assertEqual(sets.component_count, 1)


    def test_union_of_unseen_values_adds_then_connects_both(self):
        sets = DisjointSet()
        self.assertTrue(sets.union("left", "right"))
        self.assertEqual(sets.component_count, 1)
        self.assertTrue(sets.connected("left", "right"))



if __name__ == "__main__":
    unittest.main()
