def print_matrix(ls):
    for row in ls:
        print(*row, sep=" ")


def transpose_matrix(ls):
    """
    Напишите функцию для транспонирования матрицы
    :param ls:
    :return:
    """
    # print(*ls)
    # print(zip(*ls))
    # print_matrix(zip(*ls))
    return zip(*ls)


original_2D = [['o', 'x', 'o'], ['o', 'x', 'y'], ['o', 'x', 'o']]
print_matrix(original_2D)
print("-----Transpose-----")
print_matrix(transpose_matrix(original_2D))
print("-----And back-----")
print_matrix(transpose_matrix(transpose_matrix(original_2D)))



