from random import randint, choice

__all__ =["generate_any_queen","generate_correct_queen","fill_array"]
def generate_any_queen() -> tuple:
    return randint(0, 7), randint(0, 7)


def generate_correct_queen(red_moves: tuple, board_size=8) -> tuple:
    board_set = set(range(board_size))
    free_rows = board_set - red_moves[0]
    free_cols = board_set - red_moves[1]
    return choice(free_cols), choice(free_rows)


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
