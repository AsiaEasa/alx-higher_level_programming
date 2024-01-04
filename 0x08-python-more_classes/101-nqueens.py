#!/usr/bin/python3
"""Solves the N-queens puzzle."""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    bo = []
    bo = [[" " for _ in range(n)] for _ in range(n)]
    return bo


def board_deepcopy(bo):
    """Return a deepcopy"""
    if type(bo) is list:
        return list(map(board_deepcopy, bo))
    return bo


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    return [
        [r, c]
        for r in range(len(board))
        for c in range(len(board))
        if board[r][c] == "Q"
    ]


def xout(chessboard, row_played, col_played):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        chessboard (list): The current working chessboard.
        row_played (int): The row where a queen was last played.
        col_played (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col_played + 1, len(chessboard)):
        chessboard[row_played][c] = "x"
    # X out all backward spots
    for c in range(col_played - 1, -1, -1):
        chessboard[row_played][c] = "x"
    # X out all spots below
    for r in range(row_played + 1, len(chessboard)):
        chessboard[r][col_played] = "x"
    # X out all spots above
    for r in range(row_played - 1, -1, -1):
        chessboard[r][col_played] = "x"
    # X out all spots diagonally down to the right
    c = col_played + 1
    for r in range(row_played + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col_played - 1
    for r in range(row_played - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col_played + 1
    for r in range(row_played - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col_played - 1
    for r in range(row_played + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, sol):
    """Recursively solve an N-queens puzzle."""
    if queens == len(board):
        sol.append(get_solution(board))
        return sol

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            sol = recursive_solve(tmp_board, row + 1, queens + 1, sol)

    return sol


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
