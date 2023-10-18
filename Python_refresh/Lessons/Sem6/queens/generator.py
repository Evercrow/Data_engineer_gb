from random import randint, choice

__all__ = ["generate_any_queen", "generate_free_queen", "fill_array"]


def generate_any_queen() -> tuple:
    return randint(0, 7), randint(0, 7)


def generate_free_queen(free_rows: set, free_cols: set, board_size=8) -> tuple:
    return choice(tuple(free_cols)), choice(tuple(free_rows))


def fill_array(index_pairs: tuple) -> list:
    """
    Заполнение массива доски нулей ферзями-единицами из кортежа
    """
    arr = _get_zero_array()
    for pair in index_pairs:
        y = pair[0]
        x = pair[1]
        arr[y][x] = 1
    return arr


def _get_zero_array(rows=8, cols=8):
    """
    Инициализация массива шахматной доски нулями
    """
    return [[0 for _ in range(cols)] for _ in range(rows)]
