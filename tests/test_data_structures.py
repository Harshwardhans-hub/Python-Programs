"""Tests for the beginner stack and queue implementations."""

import unittest

from programs.data_structures import Queue, Stack


class StackTests(unittest.TestCase):
    def test_stack_uses_last_in_first_out_order(self):
        stack = Stack([1, 2])
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())

    def test_peek_does_not_remove_item(self):
        stack = Stack(["first"])
        self.assertEqual(stack.peek(), "first")
        self.assertEqual(len(stack), 1)

    def test_empty_stack_operations_raise_index_error(self):
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()


class QueueTests(unittest.TestCase):
    def test_queue_uses_first_in_first_out_order(self):
        queue = Queue([1, 2])
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertTrue(queue.is_empty())

    def test_peek_does_not_remove_item(self):
        queue = Queue(["first"])
        self.assertEqual(queue.peek(), "first")
        self.assertEqual(len(queue), 1)

    def test_empty_queue_operations_raise_index_error(self):
        queue = Queue()
        with self.assertRaises(IndexError):
            queue.dequeue()
        with self.assertRaises(IndexError):
            queue.peek()


if __name__ == "__main__":
    unittest.main()
