X_COORD = "abcdefghijklmnopqrstuvwxyz"


def read_position_str(pos_str: str, board_size=8) -> tuple:
    """
    Получить кортеж индексов ферзей из строки в шахматной записи
    """
    queens = pos_str.split(" ")
    pairs = []

    # if len(queens) != BOARD_SIZE:
    #     raise "Координат должно быть {BOARD_SIZE}, разделенных пробелом, проверьте строку"
    for position in queens:
        for x, y in tuple(position.split()):
            if x not in X_COORD or not (1 <= int(y) <= board_size):
                raise "Найдены неверные координаты в указанных шахматных позициях"
            else:
                # координаты начинаются в левом нижнем углу
                pairs.append((board_size - int(y), X_COORD.find(x)))
    return tuple(pairs)


def index_to_str(combo:tuple,board_size=8)->str:
    pos_str = []
    for pos in combo:
        y = str(abs(pos[0] - board_size))
        x = X_COORD[pos[1]]
        pos_str.append(x+y)
    pos_str.sort()
    return " ".join(pos_str)