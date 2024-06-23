#!/usr/bin/python3
"""
Module to determine the minimum number of coins needed to make a given amount.
"""


def makeChange(coins, amount):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    This function uses a greedy algorithm to find the minimum number of coins
    required to make up a specified amount of money. The algorithm sorts the
    coin denominations in descending order and then iteratively uses the
    largest coin denomination possible until the amount is met or determined
    to be impossible to meet with the given denominations.

    Args:
        coins (list): A list of integers representing the denominations of
                      the coins.
        amount (int): The total amount of money to make with the coins.

    Returns:
        int: The minimum number of coins needed to make the amount. If the
             amount cannot be met by any combination of the coins, returns -1.
    """
    if amount < 1:
        return 0

    # Sort the coins in descending order to try the largest denominations first
    coins.sort(reverse=True)
    count = 0  # Initialize the count of coins used

    # Iterate through the sorted list of coins
    for coin in coins:
        if amount == 0:
            break  # If the amount is zero, no more coins are needed

        # Determine the maximum number of this coin that can be used
        num = amount // coin

        # Reduce the amount by the total value of the used coins
        amount -= num * coin

        # Increase the count of coins used
        count += num
    # If the amount is zero, return the count of coins used
    # Otherwise, return -1 indicating the amount cannot be made with the
    # given coins
    return count if amount == 0 else -1
