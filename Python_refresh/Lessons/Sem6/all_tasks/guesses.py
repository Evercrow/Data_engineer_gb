from typing import Iterator
import sys
# запуск из консоли ломает импорт из своих модулей уровнем выше, нужно добавить корневую папку проекта в sys.path
from pathlib import Path
# получаем абсолютный путь к корню тремя родителями выше, если проект переносили куда-то еще
p = Path(__file__).parents[3]
sys.path.append(str(p))

from Lessons.Sem1.hw1 import guess_game

_guess_dict = dict()


# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.
def guess_game_mk2(*params) -> bool:
    if 2 <= len(params) <= 4:
        writing_list = [0, 0, 0]
        defaults = [1, 100, 10]
        params_iter = map(int, params[1:])
        for i in range(3):
            try:
                writing_list[i] = next(params_iter)
            except StopIteration:
                writing_list[i] = defaults[i]
        lower_limit, upper_limit, guess_limit = writing_list
        if lower_limit > upper_limit:
            lower_limit, upper_limit = upper_limit, lower_limit
        return guess_game(lower_limit, upper_limit, guess_limit)
    else:
        raise ParameterCount("Параметров должно быть от 1 до 3")


class ParameterCount(Exception):
    pass


def custom_guess(riddle: str, answers: list, guess_limit: int = 3) -> int:
    """
    Создайте модуль с функцией внутри.
    Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
    Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
    :return:
    """
    print(f"Загадка:\n{riddle}")
    check_answer = set(map(str, answers))
    guess_count: int = 0
    while guess_count <= guess_limit:
        guess = input("Введите вашу отгадку: ")
        if guess in check_answer:
            print("Поздравляем, вы угадали!")
            guess_log(riddle, guess_count)
            return guess_count
        else:
            print("Не отгадали")
        print(f"У вас осталось {guess_limit - 1 - guess_count} попыток")
        guess_count += 1
    else:
        print("Ваши попытки закончились, вы проиграли")
        guess_log(riddle, 0)
        return 0


# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки,
# с которой она угадана). Функция формирует словарь с информацией о результатах отгадывания. Для хранения используйте
# защищённый словарь уровня модуля. Отдельно напишите функцию, которая выводит результаты угадывания из защищённого
# словаря в удобном для чтения виде. Для формирования результатов используйте генераторное выражение.
def guess_log(riddle: str, guess_num: int):
    if riddle not in _guess_dict.keys():
        _guess_dict[riddle] = []
    _guess_dict[riddle].append(guess_num)


def print_log() -> Iterator[str]:
    return (f"{key}:{_guess_dict[key]}\n" for key in _guess_dict.keys())
