"""Tests for the singly linked list implementation."""

import unittest

from programs.linked_list import SinglyLinkedList


class SinglyLinkedListTests(unittest.TestCase):
    def test_append_and_prepend(self):
        values = SinglyLinkedList([2, 3])
        values.prepend(1)
        values.append(4)
        self.assertEqual(values.to_list(), [1, 2, 3, 4])

    def test_insert_at_beginning_middle_and_end(self):
        values = SinglyLinkedList([1, 3])
        values.insert(1, 2)
        values.insert(0, 0)
        values.insert(len(values), 4)
        self.assertEqual(values.to_list(), [0, 1, 2, 3, 4])

    def test_insert_rejects_invalid_indices(self):
        values = SinglyLinkedList([1])
        with self.assertRaises(IndexError):
            values.insert(2, 3)
        with self.assertRaises(IndexError):
            values.insert(-1, 3)
        with self.assertRaises(TypeError):
            values.insert(True, 3)

    def test_remove_first_updates_head_tail_and_length(self):
        values = SinglyLinkedList([1, 2, 2, 3])
        self.assertTrue(values.remove_first(1))
        self.assertTrue(values.remove_first(2))
        self.assertTrue(values.remove_first(3))
        self.assertEqual(values.to_list(), [2])
        self.assertEqual(len(values), 1)
        values.append(4)
        self.assertEqual(values.to_list(), [2, 4])

    def test_remove_missing_value_returns_false(self):
        values = SinglyLinkedList([1, 2])
        self.assertFalse(values.remove_first(9))
        self.assertEqual(values.to_list(), [1, 2])

    def test_search_and_empty_state(self):
        values = SinglyLinkedList(["a", "b"])
        self.assertEqual(values.search("b"), 1)
        self.assertIsNone(values.search("z"))
        self.assertTrue(values)
        self.assertFalse(SinglyLinkedList())


    def test_removing_only_node_resets_tail_before_append(self):
        values = SinglyLinkedList(["only"])
        self.assertTrue(values.remove_first("only"))
        self.assertEqual(len(values), 0)
        values.append("new tail")
        self.assertEqual(values.to_list(), ["new tail"])
        self.assertEqual(values.search("new tail"), 0)



if __name__ == "__main__":
    unittest.main()
