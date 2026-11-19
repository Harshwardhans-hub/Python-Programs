# Dynamic programming examples

The practice repository includes several dynamic-programming patterns:

- Coin change: minimum number of coins for a target amount.
- Longest increasing subsequence: longest strictly increasing subsequence length.
- 0/1 knapsack: maximize value while each item can be used at most once.
- String DP: edit distance, longest common subsequence, and longest palindromic subsequence.
- Matrix-chain ordering: minimize scalar multiplication cost by choosing parenthesization.

## Matrix-chain ordering

For matrices A1 through An, the order of multiplication changes the number of scalar operations but not the final mathematical product. `matrix_chain_order` accepts the dimensions array and returns both the minimum cost and one optimal parenthesization.

```python
from programs.matrix_chain import matrix_chain_order

cost, order = matrix_chain_order([30, 35, 15, 5, 10, 20, 25])
print(cost)   # 15125
print(order)  # ((A1(A2A3))((A4A5)A6))
```

The algorithm uses O(n²) memory and O(n³) time for n matrices.
