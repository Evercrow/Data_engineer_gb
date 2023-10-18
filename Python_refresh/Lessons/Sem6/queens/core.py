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
    if (y in red_rows) or (x in red_cols) or (x - y in red_bslash) or (x + y - BOARD_SIZE in red_slash):
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


def _place_queen(pos: tuple) -> bool:
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
        red_slash.add(x + y - BOARD_SIZE)
        return True
    else:
        return False


def _remove_queen(pos: tuple):
    """
    Убирает ферзя и его ходы с доски. Если такого ферзя нет, возвращает ошибку
    """
    x = pos[0]
    y = pos[1]

    class AlgorithmError(Exception):
        pass

    try:
        red_cols.remove(x)
        red_rows.remove(y)
        red_bslash.remove(x - y)
        red_slash.remove(x - y + BOARD_SIZE)
    except KeyError:
        raise AlgorithmError("Таких пересечений не было записано ранее")


def test_queen_combo(combo: tuple) -> bool:
    """
    Тестирует один набор ферзей на пересечение
    """
    _get_clear_board()
    for queen in combo:
        pos_check = _place_queen(queen)
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
        print(co.index_to_str(combo))
        if check:
            correct_count += 1
            p.print_board(fill_array(combo))
            print()
    return correct_count


def find_N_correct_combos(n: int) -> list:
    combos = []
    board_set = set(range(BOARD_SIZE))
    while len(combos) < n:
        _get_clear_board()
        queens = []
        while len(queens) < BOARD_SIZE:
            if len(queens) == 0:  # если доска чиста, генерируем в любой позиции
                queens.append(generate_any_queen())
                _place_queen(queens[0])
            free_rows = board_set - red_rows
            free_cols = board_set - red_cols
            new_queen = generate_free_queen(free_rows, free_cols)
            if _place_queen(new_queen):
                queens.append(new_queen)
            else:
                last_queen = _iterate_all_moves(free_rows, free_cols)
                if last_queen == tuple():
                    queens.clear()
                    break  # если в тупике, начинаем заново
                else:
                    queens.append(last_queen)
                    _place_queen(last_queen)
        if len(queens) != 0:
            combos.append(queens)
    return combos


def _iterate_all_moves(free_rows, free_cols) -> tuple:
    if free_cols == set() and free_rows == set():
        return tuple()
    for row in tuple(free_rows):
        current_cols = free_cols.copy()
        for col in tuple(free_cols):
            if _check_moves(col, row):
                return col, row
            else:
                current_cols.discard(col)
        free_rows.discard(row)
    return tuple()
