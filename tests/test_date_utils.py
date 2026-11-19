"""Tests for date range and business-day helpers."""

import unittest
from datetime import date

from programs.date_utils import add_business_days, count_business_days, date_range


class DateUtilsTests(unittest.TestCase):
    def test_date_range_is_inclusive(self):
        self.assertEqual(
            list(date_range(date(2026, 11, 20), date(2026, 11, 22))),
            [date(2026, 11, 20), date(2026, 11, 21), date(2026, 11, 22)],
        )

    def test_date_range_rejects_reversed_dates(self):
        with self.assertRaises(ValueError):
            list(date_range(date(2026, 11, 22), date(2026, 11, 20)))

    def test_business_day_count_excludes_weekends_and_holidays(self):
        self.assertEqual(
            count_business_days(
                date(2026, 11, 16), date(2026, 11, 20), holidays=[date(2026, 11, 18)]
            ),
            4,
        )

    def test_add_business_days_supports_both_directions(self):
        self.assertEqual(add_business_days(date(2026, 11, 20), 1), date(2026, 11, 23))
        self.assertEqual(add_business_days(date(2026, 11, 23), -1), date(2026, 11, 20))

    def test_zero_business_days_returns_start(self):
        self.assertEqual(add_business_days(date(2026, 11, 20), 0), date(2026, 11, 20))


if __name__ == "__main__":
    unittest.main()
