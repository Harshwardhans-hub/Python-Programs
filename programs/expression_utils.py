"""Bracket validation and arithmetic postfix evaluation without eval()."""

from collections.abc import Sequence
from numbers import Real


_BRACKETS = {")": "(", "]": "[", "}": "{"}
_OPERATORS = {"+", "-", "*", "/"}


def has_balanced_brackets(text: str) -> bool:
    """Check (), [], and {} nesting while ignoring non-bracket characters."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    opening = set(_BRACKETS.values())
    stack: list[str] = []
    for character in text:
        if character in opening:
            stack.append(character)
        elif character in _BRACKETS:
            if not stack or stack.pop() != _BRACKETS[character]:
                return False
    return not stack


def evaluate_postfix(tokens: Sequence[str | Real]) -> float:
    """Evaluate a whitespace-tokenized arithmetic postfix expression.

    Supported operators are +, -, *, and /. This function never executes code.
    Invalid token sequences raise ValueError; division by zero raises
    ZeroDivisionError.
    """
    stack: list[float] = []
    for token in tokens:
        if isinstance(token, bool):
            raise TypeError("boolean tokens are not supported")
        if isinstance(token, Real):
            stack.append(float(token))
            continue
        if not isinstance(token, str):
            raise TypeError("tokens must be numbers or strings")
        if token in _OPERATORS:
            if len(stack) < 2:
                raise ValueError("operator does not have two operands")
            right = stack.pop()
            left = stack.pop()
            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            else:
                stack.append(left / right)
        else:
            try:
                stack.append(float(token))
            except ValueError as error:
                raise ValueError(f"invalid postfix token: {token}") from error

    if len(stack) != 1:
        raise ValueError("expression must leave exactly one result")
    return stack[0]
