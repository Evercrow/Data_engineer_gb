from .core import get_zero_array

X_COORD = "abcdefgh"


def read_position_str(pos_str: str) -> tuple:
    queens = pos_str.split(" ")
    pairs = []

    if len(queens) != 8:
        raise "Координат должно быть 8, разделенных пробелом, проверьте строку"
    for position in queens:
        for x, y in tuple(position.split()):
            if x not in X_COORD or not (1 <= int(y) <= 8):
                raise "Найдены неверные координаты в указанных шахматных позициях"
            else:
                pairs.append((X_COORD.find(x), int(y) - 1))
    return tuple(pairs)


def fill_array(index_pairs: tuple) -> list:
    arr = get_zero_array()
    for pair in index_pairs:
        i = pair[0]
        j = pair[1]
        arr[i][j] = 1
    return arr
