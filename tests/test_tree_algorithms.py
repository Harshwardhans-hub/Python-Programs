"""Tests for tree symmetry, balance, and diameter."""

import unittest

from programs.tree_algorithms import diameter, is_balanced, is_symmetric
from programs.tree_utils import BinaryTreeNode


class TreeAlgorithmTests(unittest.TestCase):
    def test_symmetric_tree(self):
        root = BinaryTreeNode(
            1,
            BinaryTreeNode(2, BinaryTreeNode(3), BinaryTreeNode(4)),
            BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(3)),
        )
        self.assertTrue(is_symmetric(root))
        self.assertFalse(is_symmetric(BinaryTreeNode(1, BinaryTreeNode(2), None)))

    def test_balanced_tree(self):
        root = BinaryTreeNode(1, BinaryTreeNode(2), BinaryTreeNode(3))
        self.assertTrue(is_balanced(root))
        self.assertTrue(is_balanced(None))

    def test_unbalanced_tree(self):
        root = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(3, BinaryTreeNode(4))))
        self.assertFalse(is_balanced(root))

    def test_diameter_is_measured_in_edges(self):
        root = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)), BinaryTreeNode(3))
        self.assertEqual(diameter(root), 3)
        self.assertEqual(diameter(None), 0)


    def test_empty_and_single_node_tree_metrics(self):
        self.assertTrue(is_symmetric(None))
        self.assertTrue(is_balanced(BinaryTreeNode(7)))
        self.assertEqual(diameter(BinaryTreeNode(7)), 0)



if __name__ == "__main__":
    unittest.main()
