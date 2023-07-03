import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at the given position
    # without attacking any other queens on the board
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N  # Initialize an empty board

    def place_queen(row):
        if row == N:
            # All queens have been successfully placed, print the solution
            print([[i, board[i]] for i in range(N)])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                place_queen(row + 1)

    place_queen(0)  # Start placing queens from the first row

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve_nqueens(N)
