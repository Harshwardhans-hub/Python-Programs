"""Tests for basic input validation helpers."""

import unittest

from programs.validation_utils import is_strong_password, is_valid_email, password_feedback


class ValidationUtilsTests(unittest.TestCase):
    def test_email_format_checks(self):
        self.assertTrue(is_valid_email(" learner@example.com "))
        self.assertFalse(is_valid_email("missing-at.example.com"))
        self.assertFalse(is_valid_email("user@localhost"))
        self.assertFalse(is_valid_email(None))

    def test_password_feedback_exposes_each_independent_check(self):
        result = password_feedback("Learning7!")
        self.assertTrue(all(result.values()))
        self.assertEqual(set(result), {
            "minimum_length", "has_lowercase", "has_uppercase", "has_digit", "has_symbol"
        })

    def test_weak_password_fails_without_exposing_input(self):
        self.assertFalse(is_strong_password("password"))
        self.assertFalse(is_strong_password("12345678"))

    def test_password_helpers_validate_argument_type(self):
        with self.assertRaises(TypeError):
            password_feedback(None)
        with self.assertRaises(TypeError):
            is_strong_password(None)


if __name__ == "__main__":
    unittest.main()
