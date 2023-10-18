from . import coordinates as co, print_ as p
from .generator import *

BOARD_SIZE = 8
red_rows = set()
red_cols = set()
red_bslash = set()
red_slash = set()


def _check_moves(x: int, y: int) -> bool:
    """
    функция проверяет пересечения для конкретной клетки
    """
    if (y in red_rows) or (x in red_cols) or (x - y in red_bslash) or (x - y + BOARD_SIZE in red_slash):
        return False
    else:
        return True


def _get_clear_board():
    """
    очистка и инициализация проверочных сетов для всех "занятых" клеток на доске
    """
    global red_rows
    global red_cols
    global red_bslash
    global red_slash
    red_rows.clear()
    red_cols.clear()
    red_bslash.clear()
    red_slash.clear()


def _update_board_state(pos: tuple) -> bool:
    """
    Функция проверяет позицию ферзя, и записывает его возможные ходы на доску, если позиция корректна
    """
    x = pos[0]
    y = pos[1]
    correct = _check_moves(x, y)
    if correct:
        red_cols.add(x)
        red_rows.add(y)
        red_bslash.add(x - y)
        red_slash.add(x - y + BOARD_SIZE)
        return True
    else:
        return False


def test_queen_combo(combo: tuple) -> bool:
    """
    Тестирует один набор ферзей на пересечение
    """
    _get_clear_board()
    for queen in combo:
        pos_check = _update_board_state(queen)
        if not pos_check:
            return False
    return True


def test_and_show_combinations(combos) -> int:
    """
    Агрегатная функция для проверки набора комбинаций и распечатки только успешных.
    Возвращает количество успешных комбинаций
    """
    correct_count = 0
    for combo in combos:
        check = test_queen_combo(combo)
        p.show_check_result(check)
        print(combo)
        if check:
            correct_count += 1
            p.print_board(fill_array(combo))
            print()
    return correct_count


def find_N_correct_combos(n: int):
    combos = []
    _get_clear_board()
    while len(combos) < n:
        queens = [generate_any_queen()]

        while len(queens) < BOARD_SIZE:
            queens.append(generate_correct_queen((red_rows, red_cols)))

    return tuple(combos)
