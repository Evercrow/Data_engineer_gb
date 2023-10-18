# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

import random


def int_float_filler(f_name: str, line_num: int):
    with open(f_name, "a", encoding="UTF-8") as f:
        for i in range(line_num):
            f.write(f"{random.randint(-1000, 1000)}|{random.random() * 2000 - 1000}\n")


if __name__ == "__main__":
    int_float_filler("numbers.txt", 10)
