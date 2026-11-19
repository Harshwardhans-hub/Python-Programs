"""Number-theory algorithms useful for programming exercises."""

from math import isqrt


def sieve_primes(limit: int) -> list[int]:
    """Return all primes less than or equal to limit."""
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("limit must be an integer")
    if limit < 2:
        return []
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for candidate in range(2, isqrt(limit) + 1):
        if prime[candidate]:
            for multiple in range(candidate * candidate, limit + 1, candidate):
                prime[multiple] = False
    return [number for number, is_prime in enumerate(prime) if is_prime]


def prime_factorization(number: int) -> dict[int, int]:
    """Return prime factors mapped to their exponents for a positive integer."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 1:
        raise ValueError("number must be positive")
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= number:
        while number % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            number //= divisor
        divisor += 1 if divisor == 2 else 2
    if number > 1:
        factors[number] = factors.get(number, 0) + 1
    return factors


def modular_power(base: int, exponent: int, modulus: int) -> int:
    """Compute (base ** exponent) % modulus using repeated squaring."""
    for name, value in (("base", base), ("exponent", exponent), ("modulus", modulus)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
    if exponent < 0:
        raise ValueError("exponent must be non-negative")
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    result = 1
    factor = base % modulus
    remaining = exponent
    while remaining:
        if remaining & 1:
            result = (result * factor) % modulus
        factor = (factor * factor) % modulus
        remaining >>= 1
    return result
