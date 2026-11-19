"""Tests for AVL rotations, ordering, and height balance."""

import unittest

from programs.avl_tree import AVLTree


class AVLTreeTests(unittest.TestCase):
    def test_all_four_rotation_shapes_preserve_sorted_order(self):
        for values in ([3, 2, 1], [1, 2, 3], [3, 1, 2], [1, 3, 2]):
            with self.subTest(values=values):
                tree = AVLTree(values)
                self.assertEqual(tree.in_order(), [1, 2, 3])
                self.assertEqual(tree.height, 2)

    def test_duplicate_insert_does_not_change_size(self):
        tree = AVLTree([10, 5, 15])
        self.assertFalse(tree.insert(10))
        self.assertTrue(tree.insert(12))
        self.assertEqual(len(tree), 4)
        self.assertEqual(tree.in_order(), [5, 10, 12, 15])

    def test_search_and_membership(self):
        tree = AVLTree([20, 10, 30, 5, 15])
        self.assertTrue(tree.search(15))
        self.assertIn(5, tree)
        self.assertNotIn(99, tree)

    def test_sorted_insertions_remain_balanced(self):
        tree = AVLTree(range(1, 1001))
        self.assertEqual(len(tree), 1000)
        self.assertEqual(tree.in_order(), list(range(1, 1001)))
        self.assertLessEqual(tree.height, 12)

    def test_empty_tree_contract(self):
        tree = AVLTree()
        self.assertEqual(len(tree), 0)
        self.assertEqual(tree.height, 0)
        self.assertEqual(tree.in_order(), [])
        self.assertFalse(tree.search(1))


if __name__ == "__main__":
    unittest.main()
