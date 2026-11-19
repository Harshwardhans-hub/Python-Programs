"""Tests for BFS word ladder paths."""

import unittest

from programs.word_ladder import word_ladder_length


class WordLadderTests(unittest.TestCase):
    def test_finds_shortest_sequence(self):
        words = ["hot", "dot", "dog", "lot", "log", "cog"]
        self.assertEqual(word_ladder_length("hit", "cog", words), 5)

    def test_missing_target_or_disconnected_dictionary_returns_none(self):
        self.assertIsNone(word_ladder_length("hit", "cog", ["hot", "dot", "dog"]))
        self.assertIsNone(word_ladder_length("hit", "cog", ["cog", "aaa", "bbb"]))

    def test_same_start_and_end_has_length_one(self):
        self.assertEqual(word_ladder_length("same", "same", []), 1)

    def test_dictionary_words_of_other_lengths_are_ignored(self):
        self.assertEqual(word_ladder_length("a", "c", ["long", "b", "c"]), 3)

    def test_invalid_endpoint_and_dictionary_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            word_ladder_length("", "a", [])
        with self.assertRaises(ValueError):
            word_ladder_length("a", "long", [])
        with self.assertRaises(TypeError):
            word_ladder_length("a", "b", ["b", 1])


if __name__ == "__main__":
    unittest.main()
