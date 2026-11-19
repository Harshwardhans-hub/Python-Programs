"""Tests for LCS, edit distance, and palindromic subsequences."""

import unittest

from programs.string_dp import (
    edit_distance,
    longest_common_subsequence_length,
    longest_palindromic_subsequence_length,
)


class StringDynamicProgrammingTests(unittest.TestCase):
    def test_lcs_length(self):
        self.assertEqual(longest_common_subsequence_length("abcde", "ace"), 3)
        self.assertEqual(longest_common_subsequence_length("", "abc"), 0)

    def test_edit_distance(self):
        self.assertEqual(edit_distance("kitten", "sitting"), 3)
        self.assertEqual(edit_distance("same", "same"), 0)
        self.assertEqual(edit_distance("", "abc"), 3)

    def test_longest_palindromic_subsequence(self):
        self.assertEqual(longest_palindromic_subsequence_length("bbbab"), 4)
        self.assertEqual(longest_palindromic_subsequence_length("cbbd"), 2)
        self.assertEqual(longest_palindromic_subsequence_length(""), 0)

    def test_string_type_validation(self):
        with self.assertRaises(TypeError):
            edit_distance("a", 5)


if __name__ == "__main__":
    unittest.main()
