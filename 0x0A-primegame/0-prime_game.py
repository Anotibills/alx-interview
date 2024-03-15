#!/usr/bin/python3
"""
This is the prime game winner determination
"""


def isWinner(x, nums):
    """
    This determine winner of each round and the player who won the most rounds.
    """
    if x < 1 or not nums:
        return None

    m_wins = 0
    b_wins = 0

    for n in nums:
        if n == 1:
            b_wins += 1
            continue

        # Check if Maria can make a move
        if n % 2 == 0:
            m_wins += 1
            continue

        # Check if Ben can make a move
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                b_wins += 1
                break
        else:
            m_wins += 1

    if m_wins == b_wins:
        return None

    return 'Maria' if m_wins > b_wins else 'Ben'


if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    print(isWinner(x, nums))  # Output: Ben
