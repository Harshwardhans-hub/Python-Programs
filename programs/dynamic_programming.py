"""Classic dynamic-programming exercises with small, explicit contracts."""

from collections.abc import Sequence


def minimum_coin_change(coins: Sequence[int], amount: int) -> int | None:
    """Return the fewest coins needed, or None when the amount is unreachable."""
    if isinstance(amount, bool) or not isinstance(amount, int):
        raise TypeError("amount must be an integer")
    if amount < 0:
        raise ValueError("amount cannot be negative")
    if any(isinstance(coin, bool) or not isinstance(coin, int) for coin in coins):
        raise TypeError("coin denominations must be integers")
    if any(coin <= 0 for coin in coins):
        raise ValueError("coin denominations must be positive")
    best = [0] + [amount + 1] * amount
    for current in range(1, amount + 1):
        for coin in coins:
            if coin <= current:
                best[current] = min(best[current], best[current - coin] + 1)
    return best[amount] if best[amount] <= amount else None


def longest_increasing_subsequence_length(values: Sequence[int]) -> int:
    """Return the length of the longest strictly increasing subsequence."""
    if not values:
        return 0
    lengths = [1] * len(values)
    for index in range(len(values)):
        for previous in range(index):
            if values[previous] < values[index]:
                lengths[index] = max(lengths[index], lengths[previous] + 1)
    return max(lengths)


def zero_one_knapsack(weights: Sequence[int], values: Sequence[int], capacity: int) -> int:
    """Return the maximum value for a 0/1 knapsack with integer weights."""
    if len(weights) != len(values):
        raise ValueError("weights and values must have equal lengths")
    if isinstance(capacity, bool) or not isinstance(capacity, int):
        raise TypeError("capacity must be an integer")
    if capacity < 0:
        raise ValueError("capacity cannot be negative")
    if any(isinstance(weight, bool) or not isinstance(weight, int) for weight in weights):
        raise TypeError("weights must be integers")
    if any(weight < 0 for weight in weights):
        raise ValueError("weights cannot be negative")

    best = [0] * (capacity + 1)
    for weight, value in zip(weights, values):
        for current_capacity in range(capacity, weight - 1, -1):
            best[current_capacity] = max(
                best[current_capacity],
                best[current_capacity - weight] + value,
            )
    return best[capacity]
