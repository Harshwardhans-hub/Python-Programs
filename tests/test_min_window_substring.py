"""Tests for minimum window substring search."""

import unittest

from programs.min_window_substring import minimum_window_substring


class MinimumWindowSubstringTests(unittest.TestCase):
    def test_finds_minimum_window_with_duplicate_requirements(self):
        self.assertEqual(minimum_window_substring("ADOBECODEBANC", "ABC"), "BANC")
        self.assertEqual(minimum_window_substring("aaabdabcefaecbef", "abc"), "abc")

    def test_character_multiplicity_is_required(self):
        self.assertEqual(minimum_window_substring("abcbcba", "aabc"), "abcb cba".replace(" ", ""))
        self.assertEqual(minimum_window_substring("abc", "aabc"), "")

    def test_empty_and_oversized_targets_return_empty(self):
        self.assertEqual(minimum_window_substring("abc", ""), "")
        self.assertEqual(minimum_window_substring("a", "ab"), "")
        self.assertEqual(minimum_window_substring("", "a"), "")

    def test_unicode_text_is_supported(self):
        self.assertEqual(minimum_window_substring("x🙂a🙂b", "🙂b"), "🙂b")

    def test_non_string_inputs_are_rejected(self):
        with self.assertRaises(TypeError):
            minimum_window_substring(None, "a")
        with self.assertRaises(TypeError):
            minimum_window_substring("abc", 1)


if __name__ == "__main__":
    unittest.main()
