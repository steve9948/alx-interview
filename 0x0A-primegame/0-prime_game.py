#!/usr/bin/python3
"""0. Prime Game"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for multiple in range(p*p, n + 1, p):
                sieve[multiple] = False
    return [num for num in range(2, n + 1) if sieve[num]]

def isWinner(x, nums):
    """
    Determines the winner of Prime Game
    x: the number of rounds
    nums: list of the upper limit of ranges for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x < 1 or not nums:
        return None

    Maria = 0
    Ben = 0

    for n in nums:
        prime_count = len(primes(n))
        if prime_count % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return "Maria"
    elif Ben > Maria:
        return "Ben"
    return None
