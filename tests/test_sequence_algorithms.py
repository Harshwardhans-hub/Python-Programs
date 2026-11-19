"""Tests for consecutive sequence, majority element, and stock profit."""

import unittest

from programs.sequence_algorithms import (
    longest_consecutive_sequence_length,
    majority_element,
    maximum_single_transaction_profit,
)


class SequenceAlgorithmTests(unittest.TestCase):
    def test_longest_consecutive_sequence(self):
        self.assertEqual(longest_consecutive_sequence_length([100, 4, 200, 1, 3, 2]), 4)
        self.assertEqual(longest_consecutive_sequence_length([]), 0)

    def test_majority_element(self):
        self.assertEqual(majority_element([2, 2, 1, 2]), 2)
        self.assertIsNone(majority_element([1, 2, 3]))

    def test_maximum_single_transaction_profit(self):
        self.assertEqual(maximum_single_transaction_profit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(maximum_single_transaction_profit([7, 6, 4, 3]), 0)
        self.assertEqual(maximum_single_transaction_profit([]), 0)


    def test_majority_element_singleton_and_empty_sequences(self):
        self.assertEqual(majority_element([42]), 42)
        self.assertIsNone(majority_element([]))

    def test_consecutive_sequence_handles_negative_values_and_duplicates(self):
        self.assertEqual(longest_consecutive_sequence_length([-3, -2, -2, -1, 7]), 3)



if __name__ == "__main__":
    unittest.main()
