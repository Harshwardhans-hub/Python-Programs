"""Tests for bit counting, power-of-two, and XOR helpers."""

import unittest

from programs.bitwise_utils import count_set_bits, is_power_of_two, single_number


class BitwiseUtilsTests(unittest.TestCase):
    def test_count_set_bits(self):
        self.assertEqual(count_set_bits(0), 0)
        self.assertEqual(count_set_bits(0b101101), 4)

    def test_power_of_two(self):
        self.assertTrue(is_power_of_two(1))
        self.assertTrue(is_power_of_two(1024))
        self.assertFalse(is_power_of_two(0))
        self.assertFalse(is_power_of_two(12))

    def test_single_number(self):
        self.assertEqual(single_number([4, 1, 2, 1, 2]), 4)

    def test_negative_and_boolean_values_are_rejected(self):
        with self.assertRaises(ValueError):
            count_set_bits(-1)
        with self.assertRaises(TypeError):
            is_power_of_two(True)


    def test_large_integer_and_empty_sequence_boundaries(self):
        self.assertEqual(count_set_bits(1 << 80), 1)
        self.assertEqual(single_number([]), 0)
        self.assertFalse(is_power_of_two(3 * (1 << 20)))

    def test_single_number_validates_each_value(self):
        with self.assertRaises(ValueError):
            single_number([1, -1, 2])
        with self.assertRaises(TypeError):
            single_number([1, True])



if __name__ == "__main__":
    unittest.main()
