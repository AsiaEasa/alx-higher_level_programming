#!/usr/bin/python3
"""Solves the N-queens puzzle."""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    bo = []
    bo = [[' ' for _ in range(n)] for _ in range(n)]
    return (bo)


def board_deepcopy(bo):
    """Return a deepcopy"""
    if type(bo) is list:
        return list(map(board_deepcopy, bo))
    return (bo)


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    return [
        [r, c]
        for r in range(len(board))
        for c in range(len(board)) if board[r][c] == "Q"
    ]


def xout(board, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    def is_safe(board, row, col):
        """Check if placing a queen at a specific position is safe."""
        return all(board[i] != col and board[i] - i != col - row and board[i] + i != col + row for i in range(row))

    def place_queen(board, row, solutions):
        """Place queens recursively on the board."""
        if row == n:
            solutions.append(board[:])  # Append a copy of the solution
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                place_queen(board, row + 1, solutions)

    solutions = []
    place_queen([-1] * n, 0, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
