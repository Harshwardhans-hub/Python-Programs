"""Tests for bracket validation and postfix evaluation."""

import unittest

from programs.expression_utils import evaluate_postfix, has_balanced_brackets


class ExpressionUtilsTests(unittest.TestCase):
    def test_balanced_brackets_allow_text_between_pairs(self):
        self.assertTrue(has_balanced_brackets("call([item{index}])"))
        self.assertTrue(has_balanced_brackets("no brackets here"))

    def test_mismatched_or_unclosed_brackets_fail(self):
        self.assertFalse(has_balanced_brackets("([)]"))
        self.assertFalse(has_balanced_brackets("((("))
        self.assertFalse(has_balanced_brackets("]"))

    def test_postfix_evaluates_all_supported_operators(self):
        self.assertEqual(evaluate_postfix(["2", "3", "+", "4", "*"]), 20.0)
        self.assertEqual(evaluate_postfix([10, 3, "-"]), 7.0)
        self.assertEqual(evaluate_postfix(["8", "2", "/"]), 4.0)

    def test_postfix_rejects_invalid_expressions_and_tokens(self):
        for expression in ([], ["+"], ["2", "3"], ["2", "bad", "+"]):
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    evaluate_postfix(expression)
        with self.assertRaises(ZeroDivisionError):
            evaluate_postfix(["1", "0", "/"])
        with self.assertRaises(TypeError):
            evaluate_postfix([True])


    def test_postfix_evaluation_respects_operand_order(self):
        self.assertEqual(evaluate_postfix(["10", "3", "2", "/", "-"]), 8.5)

    def test_postfix_rejects_code_like_strings_as_invalid_tokens(self):
        with self.assertRaises(ValueError):
            evaluate_postfix(["__import__('os')"])



if __name__ == "__main__":
    unittest.main()
