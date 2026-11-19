"""Dynamic programming for optimal matrix-chain multiplication order."""

from collections.abc import Sequence


def matrix_chain_order(dimensions: Sequence[int]) -> tuple[int, str]:
    """Return minimum scalar multiplication cost and an optimal parenthesization.

    dimensions [d0, d1, ..., dn] describe matrices A1..An where Ai has
    shape d(i-1) × di. The input must contain at least one matrix and all
    dimensions must be positive integers.
    """
    if isinstance(dimensions, (str, bytes)) or not isinstance(dimensions, Sequence):
        raise TypeError("dimensions must be a sequence of integers")
    if len(dimensions) < 2:
        raise ValueError("at least one matrix dimension pair is required")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in dimensions):
        raise TypeError("matrix dimensions must be integers")
    if any(value <= 0 for value in dimensions):
        raise ValueError("matrix dimensions must be positive")

    count = len(dimensions) - 1
    cost = [[0] * count for _ in range(count)]
    split = [[-1] * count for _ in range(count)]

    for chain_length in range(2, count + 1):
        for start in range(count - chain_length + 1):
            end = start + chain_length - 1
            best = float("inf")
            for middle in range(start, end):
                candidate = (
                    cost[start][middle]
                    + cost[middle + 1][end]
                    + dimensions[start] * dimensions[middle + 1] * dimensions[end + 1]
                )
                if candidate < best:
                    best = candidate
                    split[start][end] = middle
            cost[start][end] = int(best)

    def build(start: int, end: int) -> str:
        if start == end:
            return f"A{start + 1}"
        middle = split[start][end]
        return f"({build(start, middle)}{build(middle + 1, end)})"

    return cost[0][count - 1], build(0, count - 1)
