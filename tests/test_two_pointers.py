"""Tests for two-pointer array and string helpers."""

import unittest

from programs.two_pointers import is_text_palindrome, two_sum_sorted, unique_sorted_values


class TwoPointerTests(unittest.TestCase):
    def test_two_sum_sorted(self):
        values = [1, 2, 4, 7, 11]
        self.assertEqual(two_sum_sorted(values, 9), (1, 3))
        self.assertIsNone(two_sum_sorted(values, 40))

    def test_two_sum_handles_duplicate_values(self):
        self.assertEqual(two_sum_sorted([2, 2, 3], 4), (0, 1))

    def test_unique_sorted_values(self):
        self.assertEqual(unique_sorted_values([1, 1, 2, 2, 2, 4]), [1, 2, 4])
        self.assertEqual(unique_sorted_values([]), [])

    def test_text_palindrome_ignores_spaces_and_punctuation(self):
        self.assertTrue(is_text_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_text_palindrome("hello"))

    def test_text_palindrome_type_validation(self):
        with self.assertRaises(TypeError):
            is_text_palindrome(123)


if __name__ == "__main__":
    unittest.main()
