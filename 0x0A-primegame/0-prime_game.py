#!/usr/bin/python3
"""0. Prime Game"""


def primes(n):
    """
    Return a list of prime numbers between 1 and n inclusive.

    Args:
        n (int): The upper limit of the range to find primes.

    Returns:
        list: A list of prime numbers between 1 and n inclusive.
    """
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            for multiple in range(p*p, n + 1, p):
                sieve[multiple] = False
    return [num for num in range(2, n + 1) if sieve[num]]


def isWinner(x, nums):
    """
    Determines the overall winner of the Prime Game after x rounds.

    Args:
        x (int): The number of rounds to be played.
        nums (list): A list of integers where each integer represents the upper
                     limit of the range of numbers for that round.

    Returns:
        str: The name of the player with the most wins ('Maria' or 'Ben').
             Returns None if there is a tie or if the input is invalid.
    """
    if x < 1 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = len(primes(n))
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
