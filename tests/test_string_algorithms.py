"""Tests for reusable string algorithm helpers."""

import unittest

from programs.string_algorithms import (
    first_unique_character_index,
    is_anagram,
    longest_common_prefix,
    run_length_decode,
    run_length_encode,
)


class StringAlgorithmTests(unittest.TestCase):
    def test_anagram_ignores_case_and_punctuation(self):
        self.assertTrue(is_anagram("Dormitory", "Dirty room!!"))
        self.assertFalse(is_anagram("hello", "world"))

    def test_first_unique_character_index(self):
        self.assertEqual(first_unique_character_index("swiss"), 1)
        self.assertIsNone(first_unique_character_index("aabb"))

    def test_longest_common_prefix(self):
        self.assertEqual(longest_common_prefix(["flower", "flow", "flight"]), "fl")
        self.assertEqual(longest_common_prefix(["dog", "racecar", "car"]), "")
        self.assertEqual(longest_common_prefix([]), "")

    def test_run_length_round_trip(self):
        encoded = run_length_encode("aaabbccccd")
        self.assertEqual(encoded, [("a", 3), ("b", 2), ("c", 4), ("d", 1)])
        self.assertEqual(run_length_decode(encoded), "aaabbccccd")

    def test_run_length_empty_string(self):
        self.assertEqual(run_length_encode(""), [])
        self.assertEqual(run_length_decode([]), "")

    def test_run_length_decode_rejects_invalid_entries(self):
        with self.assertRaises(ValueError):
            run_length_decode([("ab", 2)])
        with self.assertRaises(ValueError):
            run_length_decode([("a", -1)])


if __name__ == "__main__":
    unittest.main()
