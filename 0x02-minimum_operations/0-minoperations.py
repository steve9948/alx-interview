#!/usr/bin/python3
"""
0. Minimum Operations
"""


def minOperations(n):
    """
    Calculate the minimum number of operations to get
    exactly `n` 'H' characters.

    Parameters:
    n (int): The target number of 'H' characters.

    Returns:
    int: Minimum number of operations needed.
         Returns 0 if `n` <= 1.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        if n % factor == 0:
            while n % factor == 0:
                n //= factor
                operations += factor
        factor += 1

    return operations
