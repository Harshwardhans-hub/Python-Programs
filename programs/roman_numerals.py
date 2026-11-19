"""Convert between integers and canonical Roman numerals (1 through 3999)."""


_VALUES = (
    (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
)
_LOOKUP = {symbol: value for value, symbol in _VALUES}


def to_roman(number: int) -> str:
    """Convert an integer in the canonical Roman numeral range to text."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if not 1 <= number <= 3999:
        raise ValueError("number must be between 1 and 3999")
    remaining = number
    parts: list[str] = []
    for value, symbol in _VALUES:
        count, remaining = divmod(remaining, value)
        parts.extend([symbol] * count)
    return "".join(parts)


def from_roman(numeral: str) -> int:
    """Parse a canonical Roman numeral, accepting lowercase input."""
    if not isinstance(numeral, str):
        raise TypeError("numeral must be a string")
    normalized = numeral.upper()
    if not normalized:
        raise ValueError("numeral cannot be empty")
    total = 0
    index = 0
    while index < len(normalized):
        current = _LOOKUP.get(normalized[index])
        if current is None:
            raise ValueError("numeral contains an invalid symbol")
        if index + 1 < len(normalized):
            following = _LOOKUP.get(normalized[index + 1])
            if following is None:
                raise ValueError("numeral contains an invalid symbol")
            if current < following:
                total += following - current
                index += 2
                continue
        total += current
        index += 1
    if not 1 <= total <= 3999 or to_roman(total) != normalized:
        raise ValueError("numeral is not in canonical Roman form")
    return total
