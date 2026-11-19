"""Tests for the existing text processing helpers."""

import unittest

from programs.text_utils import is_palindrome, normalize_whitespace, word_frequency


class TextUtilsTests(unittest.TestCase):
    def test_normalize_whitespace_collapses_and_trims(self):
        self.assertEqual(normalize_whitespace("  learn   Python\n daily "), "learn Python daily")
        self.assertEqual(normalize_whitespace("   "), "")

    def test_palindrome_ignores_punctuation_and_case(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))
        self.assertFalse(is_palindrome("Python is fun"))

    def test_word_frequency_is_case_insensitive(self):
        self.assertEqual(word_frequency("Python python SQL"), {"python": 2, "sql": 1})

    def test_helpers_reject_non_string_inputs(self):
        for helper in (normalize_whitespace, is_palindrome, word_frequency):
            with self.subTest(helper=helper.__name__):
                with self.assertRaises(TypeError):
                    helper(None)


if __name__ == "__main__":
    unittest.main()
