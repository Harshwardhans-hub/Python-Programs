"""Tests for KMP substring search."""

import unittest

from programs.string_search import find_all_occurrences


class StringSearchTests(unittest.TestCase):
    def test_finds_single_and_multiple_occurrences(self):
        self.assertEqual(find_all_occurrences("ababcabc", "abc"), [2, 5])
        self.assertEqual(find_all_occurrences("aaaaa", "aa"), [0, 1, 2, 3])

    def test_returns_empty_when_pattern_is_absent(self):
        self.assertEqual(find_all_occurrences("python", "java"), [])

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            find_all_occurrences("text", "")
        with self.assertRaises(TypeError):
            find_all_occurrences(10, "1")


    def test_empty_text_long_pattern_and_unicode(self):
        self.assertEqual(find_all_occurrences("", "a"), [])
        self.assertEqual(find_all_occurrences("ab", "abcd"), [])
        self.assertEqual(find_all_occurrences("café café", "café"), [0, 5])

    def test_prefix_fallback_finds_match_after_partial_overlap(self):
        self.assertEqual(find_all_occurrences("bacbabababacaca", "ababaca"), [6])



if __name__ == "__main__":
    unittest.main()
