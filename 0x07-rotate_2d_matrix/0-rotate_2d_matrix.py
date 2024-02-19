#!/usr/bin/python3
"""
A function of 2D matrix that rotate in 90 degrees clockwise and return nothing
"""


def rotate_2d_matrix(matrix):
    '''
    This defines a function that rotates 2D matrix
    '''
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            x = n - 1 - j
            temp = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[n - i - 1][x]
            matrix[n - i - 1][x] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
