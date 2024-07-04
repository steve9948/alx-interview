#!/usr/bin/python3
"""0. Prime Game"""


def generatePrimeNumbers(limit):
    """
    Return a list of prime numbers between 1 and n inclusive.

    Args:
        n (int): The upper limit of the range to find primes.

    Returns:
        list: A list of prime numbers between 1 and n inclusive.
    """
    primeNumbers = []
    sieveList = [True] * (limit + 1)
    for potentialPrime in range(2, limit + 1):
        if sieveList[potentialPrime]:
            primeNumbers.append(potentialPrime)
            for multiple in range(potentialPrime, limit + 1, potentialPrime):
                sieveList[multiple] = False
    return primeNumbers


def isWinner(numRounds, roundValues):
    """
    Determines the overall winner of the Prime Game after x rounds.

    Args:
        i (int): The number of rounds to be played.
        nums (list): A list of integers where each integer represents the upper
                     limit of the range of numbers for that round.

    Returns:
        str: The name of the player with the most wins ('Maria' or 'Ben').
             Returns None if there is a tie or if the input is invalid.
    """
    if not numRounds or not roundValues:
        return None
    mariaScore = benScore = 0
    for i in range(numRounds):
        primes = generatePrimeNumbers(roundValues[i])
        if len(primes) % 2 == 0:
            benScore += 1
        else:
            mariaScore += 1
    if mariaScore > benScore:
        return "Maria"
    elif benScore > mariaScore:
        return "Ben"
    return None
