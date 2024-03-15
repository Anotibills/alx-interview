#!/usr/bin/python3
"""
This is the prime game winner determination
"""


def isWinner(x, nums):
    '''
    This determines the best result
    '''
    score = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]
    add_prime(max(nums), primes)

    for round in range(x):
        _sum=sum((i!=0)*(i<=nums[round])for i in primes[:nums[round]+1])
        if _sum % 2:
            winner = "Maria"
        else:
            winner = "Ben"
        if winner == "Maria":
            score["Maria"] += 1
        elif winner == "Ben":
            score["Ben"] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"

    return None
