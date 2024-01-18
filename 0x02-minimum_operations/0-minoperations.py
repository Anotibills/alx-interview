#!/usr/bin/python3
"""
A method that calculates the fewest number of operations needed to result
"""


def minOperations(n):
    '''
    This returns the minimum operations to get n H's
    '''
    min_operations = 0

    if n <= 1:
        return min_operations

    if not isinstance(n, int) or n < 2:
        return 0

    for i in range(2, n + 1):
        while n % i == 0:
            min_operations += i
            n //= i

    return min_operations


if __name__ == '__main__':
    from random import randint
    from time import time

    start_time = time()

    for _ in range(10):
        random_n = randint(2, 100)
        print("Min # of operations to reach {} char: {}".
              format(random_n, minOperations(random_n)))

    print(f'==> Program completed in {time() - start_time:.3f}s')
