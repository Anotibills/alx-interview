#!/usr/bin/python3
"""
This is the prime game winner determination
"""


def generate_primes(n):
    """ Generate primes up to n """
    primes = [2]
    for i in range(3, n + 1, 2):
        is_prime = True
        for j in range(3, int(i ** 0.5) + 1, 2):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    This returns the name of the player that won the most rounds
    If the winner cannot be determined, return None
    """

    score = {"Maria": 0, "Ben": 0}
    max_num = max(nums)
    primes = generate_primes(max_num)

    for round_num in range(x):
        round_score = sum(1 for prime in primes if prime <= nums[round_num])
        winner = "Maria" if round_score % 2 != 0 else "Ben"
        score[winner] += 1

    return max(score, key=score.get) if score["Maria"] != score["Ben"] else None
