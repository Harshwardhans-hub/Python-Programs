"""Tests for hash-map lookup and grouping helpers."""

import unittest

from programs.hashing_utils import group_anagrams, two_sum


class HashingUtilsTests(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))
        self.assertEqual(two_sum([3, 3], 6), (0, 1))
        self.assertIsNone(two_sum([1, 2, 3], 10))

    def test_group_anagrams_preserves_group_order(self):
        self.assertEqual(
            group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
            [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
        )

    def test_empty_group_and_type_validation(self):
        self.assertEqual(group_anagrams([]), [])
        with self.assertRaises(TypeError):
            group_anagrams(["ok", 1])


if __name__ == "__main__":
    unittest.main()
