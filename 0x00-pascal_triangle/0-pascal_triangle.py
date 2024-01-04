#!/usr/bin/python3
"""Function that returns the integer of Pascal's Triangle"""


def pascal_triangle(n):
    """
    This returns integers in the Pascal’s triangle
    """
    if n <= 0:
        return []

    pascal = [[1]]
    while len(pascal) != n:
        previous = pascal[-1]
        current = [1]
        for li in range(len(previous) - 1):
            current.append(previous[li] + previous[li + 1])
        current.append(1)
        pascal.append(current)
    return pascal
