#!/usr/bin/python3
"""0. Prime Game"""


def isWinner(x, nums):
    if not nums or x < 1:
        return None

    def sieve(n):
        """Return a list of primes up to n."""
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    max_n = max(nums)
    primes = sieve(max_n)
    prime_set = set(primes)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        current_numbers = list(range(1, n + 1))
        turn = 0  # 0 for Maria, 1 for Ben

        while True:
            found_prime = False
            for num in current_numbers:
                if num in prime_set:
                    found_prime = True
                    prime = num
                    break

            if not found_prime:
                if turn == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            multiples = [i for i in current_numbers if i % prime == 0]
            for multiple in multiples:
                current_numbers.remove(multiple)

            turn = 1 - turn  # switch turns

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
