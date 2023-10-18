import string

from .generator import *

EMPTY = "|   "
QUEEN = "| Q "
BORDER = "+---"
COORD_X = string.ascii_uppercase
SIZE = 8


def print_board(board: list[int]):
    print(BORDER * SIZE, end="+\n")
    for row in range(SIZE):
        for col in range(SIZE):
            print(f'{EMPTY if board[row][col] == 0 else QUEEN}', end='')
        print(f"| {SIZE - row}")
        print(BORDER * SIZE, end="+\n")
    for l in COORD_X[:SIZE]:
        print(f"| {l} ", end="")
    print()


def show_check_result(flag: bool):
    print(f"Такая комбинация ферзей {'' if flag else 'не'}верная")


def print_combo(combo: tuple):
    print_board(fill_array(combo))
