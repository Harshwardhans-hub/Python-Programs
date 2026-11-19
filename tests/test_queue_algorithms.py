"""Tests for deque-based sliding-window maximum."""

import unittest

from programs.queue_algorithms import sliding_window_maximum


class QueueAlgorithmTests(unittest.TestCase):
    def test_sliding_window_maximum(self):
        self.assertEqual(
            sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3),
            [3, 3, 5, 5, 6, 7],
        )

    def test_window_larger_than_sequence_returns_empty(self):
        self.assertEqual(sliding_window_maximum([1, 2], 3), [])

    def test_invalid_window_size_is_rejected(self):
        with self.assertRaises(ValueError):
            sliding_window_maximum([1, 2], 0)
        with self.assertRaises(TypeError):
            sliding_window_maximum([1, 2], True)


if __name__ == "__main__":
    unittest.main()
