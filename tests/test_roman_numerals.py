"""Tests for canonical Roman numeral conversions."""

import unittest

from programs.roman_numerals import from_roman, to_roman


class RomanNumeralTests(unittest.TestCase):
    def test_known_integer_conversions(self):
        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(944), "CMXLIV")
        self.assertEqual(to_roman(3999), "MMMCMXCIX")

    def test_round_trip_for_representative_values(self):
        for number in (4, 9, 58, 1994, 2026, 3888):
            with self.subTest(number=number):
                self.assertEqual(from_roman(to_roman(number)), number)

    def test_parser_accepts_lowercase(self):
        self.assertEqual(from_roman("mmxxvi"), 2026)

    def test_invalid_and_noncanonical_values_are_rejected(self):
        for numeral in ("", "IIII", "VX", "MMMM", "ABC"):
            with self.subTest(numeral=numeral):
                with self.assertRaises(ValueError):
                    from_roman(numeral)
        with self.assertRaises(ValueError):
            to_roman(0)
        with self.assertRaises(TypeError):
            to_roman(True)


    def test_round_trip_for_entire_supported_domain(self):
        for number in range(1, 4000):
            with self.subTest(number=number):
                self.assertEqual(from_roman(to_roman(number)), number)



if __name__ == "__main__":
    unittest.main()
