#!/usr/bin/python3
"""
A method that calculates the fewest number of operations needed to result
"""
import math


def factors(n):
    '''
    This returns the factors of n.
    '''
    my_list = []
    while n % 2 == 0:
        my_list.append(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            my_list.append(i)
            n //= i
    if n > 2:
        my_list.append(n)
    return my_list


def minOperations(n):
    '''
    This calculates the minimum operations.
    '''
    if not isinstance(n, int) or n < 2:
        return 0
    else:
        num_operations = sum(factors(n))
        return int(num_operations)


if __name__ == '__main__':
    from random import randint
    from time import time

    start_time = time()

    for _ in range(10):
        random_n = randint(2, 100)
        print("Min # of operations to reach {} char: {}".
              format(random_n, minOperations(random_n)))

    print(f'==> Program completed in {time() - start_time:.3f}s')
