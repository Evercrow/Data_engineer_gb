from .generator import *

EMPTY = "|   "
QUEEN = "| Q "
BORDER = "+---"


def print_board(board: list[int]):
    print(BORDER * 8, end="+\n")
    for row in range(8):
        for col in range(8):
            print(f'{EMPTY if board[row][col] == 0 else QUEEN}', end='')
        print("|")
        print(BORDER * 8, end="+\n")


def show_check_result(flag: bool):
    print(f"Такая комбинация ферзей {'' if flag else 'не'}верная")


def print_combo(combo: tuple):
    print_board(fill_array(combo))
