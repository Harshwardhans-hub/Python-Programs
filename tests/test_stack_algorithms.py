"""Tests for bracket validation and next-greater elements."""

import unittest

from programs.stack_algorithms import balanced_brackets, next_greater_elements


class StackAlgorithmTests(unittest.TestCase):
    def test_balanced_brackets(self):
        self.assertTrue(balanced_brackets("function(a[0], {b: 1})"))
        self.assertTrue(balanced_brackets("plain text"))
        self.assertFalse(balanced_brackets("([)]"))
        self.assertFalse(balanced_brackets("((("))

    def test_balanced_brackets_requires_text(self):
        with self.assertRaises(TypeError):
            balanced_brackets(123)

    def test_next_greater_elements(self):
        self.assertEqual(
            next_greater_elements([4, 5, 2, 10, 8]),
            [5, 10, 10, None, None],
        )

    def test_next_greater_elements_handles_empty_and_equal_values(self):
        self.assertEqual(next_greater_elements([]), [])
        self.assertEqual(next_greater_elements([2, 2]), [None, None])


if __name__ == "__main__":
    unittest.main()
