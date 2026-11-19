"""Unit tests for the reusable examples in programs/."""

import tempfile
import unittest
from pathlib import Path

from programs.file_utils import count_lines, find_in_file
from programs.number_utils import (
    fibonacci_terms,
    greatest_common_divisor,
    is_prime,
    least_common_multiple,
)
from programs.text_utils import is_palindrome, normalize_whitespace, word_frequency


class NumberUtilsTests(unittest.TestCase):
    def test_prime_boundaries_and_composites(self):
        self.assertFalse(is_prime(-3))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(29))
        self.assertFalse(is_prime(49))

    def test_fibonacci_count(self):
        self.assertEqual(fibonacci_terms(0), [])
        self.assertEqual(fibonacci_terms(7), [0, 1, 1, 2, 3, 5, 8])

    def test_fibonacci_rejects_negative_count(self):
        with self.assertRaises(ValueError):
            fibonacci_terms(-1)

    def test_gcd_and_lcm(self):
        self.assertEqual(greatest_common_divisor(-54, 24), 6)
        self.assertEqual(greatest_common_divisor(0, 0), 0)
        self.assertEqual(least_common_multiple(12, 18), 36)
        self.assertEqual(least_common_multiple(0, 9), 0)


class TextUtilsTests(unittest.TestCase):
    def test_normalize_whitespace(self):
        self.assertEqual(normalize_whitespace("  hello" + chr(10) + chr(9) + "world  "), "hello world")

    def test_palindrome_ignores_punctuation_and_case(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))
        self.assertFalse(is_palindrome("Python"))

    def test_word_frequency_is_case_insensitive(self):
        self.assertEqual(word_frequency("Python python, Java!"), {"python": 2, "java": 1})


class FileUtilsTests(unittest.TestCase):
    def test_count_lines_and_find_text(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_text("First line" + chr(10) + chr(10) + "Second Line" + chr(10), encoding="utf-8")
            self.assertEqual(count_lines(path), 3)
            self.assertEqual(count_lines(path, include_blank=False), 2)
            self.assertEqual(find_in_file(path, "second", case_sensitive=False), [(3, "Second Line")])

    def test_find_rejects_empty_phrase(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_text("content", encoding="utf-8")
            with self.assertRaises(ValueError):
                find_in_file(path, "")


if __name__ == "__main__":
    unittest.main()
