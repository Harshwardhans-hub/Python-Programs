"""Tests for binary search tree insertion, lookup, traversal, and deletion."""

import unittest

from programs.binary_search_tree import BSTNode, contains, delete, inorder_values, insert


class BinarySearchTreeTests(unittest.TestCase):
    def test_insert_search_and_sorted_traversal(self):
        root = None
        for value in (5, 3, 7, 2, 4, 6, 8):
            root = insert(root, value)
        self.assertEqual(inorder_values(root), [2, 3, 4, 5, 6, 7, 8])
        self.assertTrue(contains(root, 6))
        self.assertFalse(contains(root, 10))

    def test_duplicate_insert_is_ignored(self):
        root = insert(insert(None, 4), 4)
        self.assertEqual(inorder_values(root), [4])

    def test_delete_leaf_one_child_and_two_children(self):
        root = None
        for value in (5, 3, 7, 2, 4, 6, 8):
            root = insert(root, value)
        root = delete(root, 2)
        root = delete(root, 3)
        root = delete(root, 7)
        self.assertEqual(inorder_values(root), [4, 5, 6, 8])

    def test_delete_missing_value_keeps_tree(self):
        root = insert(BSTNode(1), 2)
        root = delete(root, 5)
        self.assertEqual(inorder_values(root), [1, 2])

    def test_empty_tree_operations(self):
        self.assertEqual(inorder_values(None), [])
        self.assertFalse(contains(None, 1))
        self.assertIsNone(delete(None, 1))


if __name__ == "__main__":
    unittest.main()
