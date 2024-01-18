#!/usr/bin/env python3
"""
A method that calculates the fewest number of operations needed to result
"""
import math


def factors(n):
    """factors of n number"""
    mylist = []
    while n % 2 == 0:
        mylist.append(2)
        n = n / 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            mylist.append(i)
            n = n / i
    if n > 2:
        mylist.append(int(n))  # Convert result back to int
    return mylist


def minOperations(n):
    """calculate the minimum operations"""
    if type(n) != int or n < 2:
        return 0
    else:
        numOperations = sum(factors(n))
        return int(numOperations)
