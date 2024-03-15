#!/usr/bin/python3
""" Solve the N queens problem """

import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

board_size = int(sys.argv[1])


def find_queen_positions(board_size, row=0, col_placement=[],
                         diag_sum=[], diag_diff=[]):
    """ Find possible positions for placing queens """
    if row < board_size:
        for col in range(board_size):
            if col not in col_placement and row + col not in diag_sum\
                    and row - col not in diag_diff:
                yield from find_queen_positions(
                        board_size, row + 1, col_placement + [col],
                        diag_sum + [row + col], diag_diff + [row - col])
    else:
        yield col_placement


def solve_n_queens(board_size):
    """ Solve the N queens problem """
    queens_positions = []
    queen_index = 0
    for solution in find_queen_positions(board_size, 0):
        for col in solution:
            queens_positions.append([queen_index, col])
            queen_index += 1
        print(queens_positions)
        queens_positions = []
        queen_index = 0


solve_n_queens(board_size)
