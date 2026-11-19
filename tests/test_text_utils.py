"""Tests for text normalization helpers."""

import unittest

from programs.text_utils import is_palindrome, reverse_words, slugify, word_count


class TextUtilsTests(unittest.TestCase):
    def test_word_count_handles_whitespace_and_empty_input(self):
        self.assertEqual(word_count("  learn   Python\n daily "), 3)
        self.assertEqual(word_count("   "), 0)

    def test_slugify_normalizes_case_punctuation_and_accents(self):
        self.assertEqual(slugify("  Café & Python: Basics! "), "cafe-python-basics")

    def test_reverse_words_normalizes_whitespace(self):
        self.assertEqual(reverse_words("one   two\nthree"), "three two one")

    def test_palindrome_ignores_punctuation_and_case(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))
        self.assertFalse(is_palindrome("Python is fun"))

    def test_helpers_reject_non_string_inputs(self):
        for helper in (word_count, slugify, reverse_words, is_palindrome):
            with self.subTest(helper=helper.__name__):
                with self.assertRaises(TypeError):
                    helper(None)


if __name__ == "__main__":
    unittest.main()
