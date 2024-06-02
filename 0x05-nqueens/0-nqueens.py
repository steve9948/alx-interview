#!/usr/bin/python3
"""
N-Queens Puzzle Solver
"""

import sys


def is_valid(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if (board[i] == col or
                board[i] - i == col - row or
                board[i] + i == col + row):
            return False
    return True


def solve_nqueens(N):
    """Solve the N-Queens problem and return all solutions."""
    def backtrack(row=0):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    board = [-1] * N
    solutions = []
    backtrack()
    return solutions


def print_solutions(solutions):
    """Print the solutions in the required format."""
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    print_solutions(solutions)
