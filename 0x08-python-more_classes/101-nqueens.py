#!/usr/bin/env python3
import sys
def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
def is_valid(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i in range(row):
        if col - row + i >= 0 and board[i][col - row + i] == 1:
            return False
    for i in range(row):
        if col + row - i < len(board) and board[i][col + row - i] == 1:
            return False
    return True
def solve(board, row):
    if row == len(board):
        print_board(board)
        return
    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 1
            solve(board, row + 1)
            board[row][col] = 0
def main():
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    n = int(sys.argv[1])
    if n < 4:
        print('N must be at least 4')
        sys.exit(1)
    board = [[0] * n for _ in range(n)]
    solve(board, 0)
if __name__ == '__main__':
    main()
