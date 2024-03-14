#!/usr/bin/python3
"""
This is the prime game winner determination
"""


def isWinner(x, nums):
    """
    This determines who the winner is
    """
    if x < 1 or not nums:
        return None

    m_wins = 0
    b_wins = 0
    
    #This will generate numbers
    n = max(nums)
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for x in range(2, int(n**0.5) + 1):
        if primes[x]:
            for y in range(x**2, n + 1, x):
                primes[y] = False

    #This will count the numbers of pm less than n i nums
    for n in nums:
        count = sum(primes[2:n+1])
        b_wins += count % 2 == 0
        m_wins += count % 2 == 1

    if m_wins == b_wins:
        return None

    return 'Maria' if m_wins > b_wins else 'Ben'
