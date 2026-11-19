# Word ladder search

`word_ladder_length(begin, end, words)` returns the number of words in a shortest sequence where adjacent words differ by exactly one character.

The start word does not need to appear in the dictionary, but the target and every intermediate word must. The implementation uses breadth-first search with position-aware wildcard buckets so each candidate pattern bucket is expanded once.

- Time and memory are O(N × L) for N distinct same-length words of length L, aside from hashing costs.
- A missing or unreachable target returns `None`.
- Equal start and target strings return 1.
- Empty endpoints and unequal endpoint lengths are rejected.

Run `python -m unittest tests.test_word_ladder -v` from the repository root.
