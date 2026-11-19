"""Readable validation helpers for beginner Python projects."""

import re
from collections.abc import Mapping


_EMAIL_PATTERN = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")


def is_valid_email(value: str) -> bool:
    """Perform a practical format check; this does not verify mailbox ownership."""
    if not isinstance(value, str):
        return False
    return bool(_EMAIL_PATTERN.fullmatch(value.strip()))


def password_feedback(value: str) -> Mapping[str, bool]:
    """Return independent password checks without returning or storing the password."""
    if not isinstance(value, str):
        raise TypeError("password must be a string")
    return {
        "minimum_length": len(value) >= 8,
        "has_lowercase": any(char.islower() for char in value),
        "has_uppercase": any(char.isupper() for char in value),
        "has_digit": any(char.isdigit() for char in value),
        "has_symbol": any(not char.isalnum() and not char.isspace() for char in value),
    }


def is_strong_password(value: str) -> bool:
    """Return True only when every password feedback check passes."""
    return all(password_feedback(value).values())
