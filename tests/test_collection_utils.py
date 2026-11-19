"""Tests for chunking, stable uniqueness, rotation, and one-level flattening."""

import unittest

from programs.collection_utils import chunked, flatten_once, rotate_right, unique_preserving_order


class CollectionUtilsTests(unittest.TestCase):
    def test_chunked_keeps_last_partial_chunk(self):
        self.assertEqual(chunked([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])

    def test_chunked_rejects_invalid_sizes(self):
        with self.assertRaises(ValueError):
            chunked([1, 2], 0)
        with self.assertRaises(TypeError):
            chunked([1, 2], 1.5)

    def test_unique_preserving_order(self):
        self.assertEqual(unique_preserving_order([3, 1, 3, 2, 1]), [3, 1, 2])

    def test_rotate_right_supports_positive_and_negative_steps(self):
        self.assertEqual(rotate_right([1, 2, 3, 4], 1), [4, 1, 2, 3])
        self.assertEqual(rotate_right([1, 2, 3, 4], -1), [2, 3, 4, 1])

    def test_rotate_right_handles_empty_and_large_steps(self):
        self.assertEqual(rotate_right([], 10), [])
        self.assertEqual(rotate_right([1, 2, 3], 6), [1, 2, 3])

    def test_flatten_once_does_not_recursively_flatten(self):
        self.assertEqual(flatten_once([[1, 2], (3, 4), 5, [[6]]]), [1, 2, 3, 4, 5, [6]])


if __name__ == "__main__":
    unittest.main()
