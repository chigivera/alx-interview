#!/usr/bin/python3
"""
N Queens Puzzle Solver
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at the given position.
    
    Args:
        board (list): Current board state
        row (int): Row to check
        col (int): Column to check
        n (int): Size of the board
        
    Returns:
        bool: True if safe, False otherwise
    """
    # Check column
    for i in range(row):
        if board[i] == col:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i] == j:
            return False
    
    return True


def solve_nqueens(n):
    """
    Solve the N Queens puzzle using backtracking.
    
    Args:
        n (int): Size of the board
        
    Returns:
        list: List of all solutions
    """
    def solve(row, board, solutions):
        if row == n:
            # Convert board to solution format
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return
        
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row] = col
                solve(row + 1, board, solutions)
                board[row] = -1
    
    solutions = []
    board = [-1] * n
    solve(0, board, solutions)
    return solutions


def main():
    """Main function to handle command line arguments and print solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main() 