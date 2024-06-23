#!/usr/bin/python3
"""
Main concepts of making the coins change
"""


def makeChange(coins, total):
    """Determine the fewest coins needed to meet a given amount total.
    Args:
        coins (list): A list of the values of coins in possession.
        total (int): The amount total to be met.
    Returns:
        int: The fewest number of coins needed to meet the total. If the total
        cannot be met by any number of coins, return -1.
    """
    if total <= 0:
        return 0

    # Initialize the dp array with infinity (a large number)
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Zero coins are needed to make a total of 0

    # Iterate through all coins
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

# If dp[total] is still infinity, hence we can`t make the total given coins
    return dp[total] if dp[total] != float('inf') else -1
