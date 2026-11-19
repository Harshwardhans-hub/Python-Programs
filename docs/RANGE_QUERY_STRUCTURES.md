# Range-query data structures

This repository now includes three ways to answer range-sum questions.

| Structure | Build | Point update | Prefix sum | Arbitrary range sum |
|---|---:|---:|---:|---:|
| PrefixSum | O(n) | Not supported | O(1) | O(1) |
| FenwickTree | O(n) | O(log n) | O(log n) | O(log n) |
| SegmentTree | O(n) | O(log n) | O(log n) | O(log n) |

All range queries use inclusive start and end indexes. Indexes are zero-based. The Fenwick tree additionally accepts `prefix_sum(-1)` as the empty prefix and returns zero.

## Choosing one

- Use `PrefixSum` when the underlying sequence never changes and many range queries are expected.
- Use `FenwickTree` when point updates and prefix/range sums are the main operations.
- Use `SegmentTree` when you may later extend the aggregate operation beyond addition or need richer interval queries.

Run focused tests from the repository root:

```bash
python -m unittest tests.test_prefix_sums tests.test_fenwick_tree tests.test_segment_tree -v
```
