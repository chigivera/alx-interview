# N Queens Puzzle

This directory contains a program that solves the N Queens puzzle using backtracking.

## Files

- `0-nqueens.py`: The main script that solves the N Queens puzzle.

## Usage

To run the N Queens solver, use the following command:

```bash
./0-nqueens.py N
```

Where N is the size of the chessboard (must be at least 4).

## Example Output

For N = 4:
```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

For N = 6:
```
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```

## Algorithm

The solution uses a backtracking algorithm to find all possible ways to place N queens on an N×N chessboard such that no queen can attack another queen. The algorithm:

1. Places queens row by row
2. For each row, tries each column
3. Checks if the position is safe (no attacks)
4. Backtracks when a solution cannot be completed
5. Collects all valid solutions 