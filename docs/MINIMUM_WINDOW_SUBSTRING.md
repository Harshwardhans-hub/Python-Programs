# Minimum window substring

`minimum_window_substring(text, target)` returns the shortest contiguous part of text that contains every target character, including duplicate-character counts.

The implementation tracks how many required character frequencies are fully satisfied, then shrinks the left side while the current window remains valid. It runs in O(n + m) expected time and O(k) extra space, where k is the number of distinct target characters.

An empty target, a target longer than the source, or an impossible match returns an empty string. Character comparison is exact and case-sensitive.

Run `python -m unittest tests.test_min_window_substring -v` from the repository root.
