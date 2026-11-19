"""Tests for binary-tree traversal helpers."""

import unittest

from programs.tree_utils import BinaryTreeNode, height, inorder, level_order, postorder, preorder


class TreeUtilsTests(unittest.TestCase):
    def setUp(self):
        self.root = BinaryTreeNode(
            1,
            BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)),
            BinaryTreeNode(3),
        )

    def test_preorder_inorder_and_postorder(self):
        self.assertEqual(preorder(self.root), [1, 2, 4, 5, 3])
        self.assertEqual(inorder(self.root), [4, 2, 5, 1, 3])
        self.assertEqual(postorder(self.root), [4, 5, 2, 3, 1])

    def test_level_order(self):
        self.assertEqual(level_order(self.root), [1, 2, 3, 4, 5])

    def test_height(self):
        self.assertEqual(height(self.root), 3)
        self.assertEqual(height(None), 0)

    def test_empty_tree_traversals(self):
        self.assertEqual(preorder(None), [])
        self.assertEqual(inorder(None), [])
        self.assertEqual(postorder(None), [])
        self.assertEqual(level_order(None), [])


if __name__ == "__main__":
    unittest.main()
