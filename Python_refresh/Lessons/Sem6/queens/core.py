BOARD_SIZE = 8


def get_zero_array(rows=8, cols=8):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def check_moves(index_pairs: tuple) -> bool:
    red_rows = set()
    red_cols = set()
    red_bslash = set()
    red_slash = set()
    for pos in index_pairs:
        x = pos[0]
        y = pos[1]
        if (x in red_rows) or (y in red_cols) or (x - y in red_bslash) or (x - y + BOARD_SIZE in red_slash):
            return False
        else:
            red_rows.add(x)
            red_cols.add(y)
            red_bslash.add(x - y)
            red_slash.add(x - y + BOARD_SIZE)
    return True
