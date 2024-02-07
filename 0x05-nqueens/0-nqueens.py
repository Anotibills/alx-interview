#!/usr/bin/python3
"""
A program that solves the N queens problem
"""
import sys


class NQueen:
    '''
    This is class for solving N queens problem
    '''

    def __init__(self, n):
        '''
        This initialize variables
        '''
        self.n = n
        self.x = [0] * (n + 1)
        self.res = []

    def place(self, k, i):
        '''
        This attacks in range
        '''
        for j in range(1, k):
            if self.x[j] == i or abs(self.x[j] - i) == abs(j - k):
                return False
        return True

    def nQueen(self, k):
        '''
        This accepts args starting queen from which to evaluate
        '''
        for i in range(1, self.n + 1):
            if self.place(k, i):
                self.x[k] = i
                if k == self.n:
                    solution = []
                    for i in range(1, self.n + 1):
                        solution.append([i - 1, self.x[i] - 1])
                    self.res.append(solution)
                else:
                    self.nQueen(k + 1)
        return self.res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]

    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    queen = NQueen(N)
    res = queen.nQueen(1)

    for i in res:
        print(i)
