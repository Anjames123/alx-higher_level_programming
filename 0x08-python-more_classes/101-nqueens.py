#!/usr/bin/python3

import sys

# The main function that solves the N-Queens problem
def solveNQueens(n):
    # Check if the input n is an integer
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    # Check if the input n is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Initialize the board as a list of -1s
    board = [-1] * n
    
    # Call the recursive utility function to solve the problem
    solveNQueensUtil(board, 0, n)

# The recursive utility function that solves the N-Queens problem
def solveNQueensUtil(board, col, n):
    # Base case: all queens have been placed on the board
    if col == n:
        # Print the board configuration
        printBoard(board)
        return True
    
    # Recursive case: try to place a queen in each row of the current column
    res = False
    for row in range(n):
        if isSafe(board, row, col, n):
            board[col] = row
            res = solveNQueensUtil(board, col + 1, n) or res
            board[col] = -1
    return res

# Check if the current placement of the queen is safe
def isSafe(board, row, col, n):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

# Print the board configuration
def printBoard(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print("\n")

# Check the command line arguments and call the solveNQueens function
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

solveNQueens(n)
