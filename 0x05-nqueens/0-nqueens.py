#!/usr/bin/env python3
"""
A program that solves the N queens problem
"""
import sys


def print_board(board):
    '''
    This prints the board with queens placed.
    '''
    for row in board:
        print(' '.join(map(str, row)))


def is_safe(board, row, col, number):
    '''
    This returns true if it's safe to place a queen, False otherwise
    '''
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, number), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, number):
    '''
    This returns true if a solution is found, False otherwise
    '''
    if col == number:
        print_board(board)
        return True

    res = False
    for i in range(number):
        if is_safe(board, i, col, number):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, number) or res
            board[i][col] = 0  # Backtrack

    return res


def solve_n_queens(number):
    '''
    This returns true if a solution is found, False otherwise
    '''
    board = [[0 for _ in range(number)] for _ in range(number)]

    if not solve_n_queens_util(board, 0, number):
        return False

    return True


def validate(args):
    '''
    This returns the validated board size
    '''
    if len(args) == 2:
        try:
            number = int(args[1])
            if number < 4:
                print("N must be at least 4")
                exit(1)
            return number
        except ValueError:
            print("N must be a number")
            exit(1)
    else:
        print("Usage: nqueens N")
        exit(1)


if __name__ == "__main__":
    number = validate(sys.argv)
    solve_n_queens(number)

