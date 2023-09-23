import itertools
import math


def backpack_natural(gear: dict, max_weight=10) -> tuple:
    """
    Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
    Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
    Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.
    :param gear:
    :param max_weight:
    :return:
    """
    result = set()
    total_weight = 0
    while gear:
        item = gear.popitem()
        total_weight += item[1]
        if (max_weight - total_weight) < 0:
            total_weight -= item[1]
            continue
        elif (max_weight - total_weight) == 0:
            result.add(item[0])
            break
        else:
            result.add(item[0])
    return result, total_weight


def dict_sum_by_keys(keys, my_dict:dict)->float:
    res = 0
    for k, v in my_dict.items():
        if k in set(keys):
            res += v
    # print(set(keys),res)
    return res


def backpack_all(gear: dict, max_weight=10) -> set:
    """
    Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
    Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
    Достаточно вернуть один допустимый вариант.*Верните все возможные варианты комплектации рюкзака.
    :param gear:
    :param max_weight:
    :return:
    """
    result = set()
    # все возможные комбинации предметов , от 1 до max
    # через comprehension не получилось записать, не вижу в чем ошибка.Может,неполная запись из-за переполнения?
    # combination = { (c, dict_sum_by_keys(c, gear)) for i in range(1, len(gear))
    #                for c in itertools.combinations(gear.keys(), i) if dict_sum_by_keys(c, gear) <= max_weight }
    for i in range(1, len(gear)):
        for c in itertools.combinations(gear.keys(), i):
            t_w = dict_sum_by_keys(c, gear)
            if t_w <= max_weight:
                result.add((c, t_w))
    return result


GEAR = {
    "фляга": 0.5,
    "палатка": 4,
    "котелок": 3,
    "сухофрукты": 0.9,
    "веревка": 1.5,
    "нож": 0.5,
    "армейский паёк": 2.1,
    "бутыль с водой": 2,
    "топор": 1.5,
    "спички": 0.1,
    "жидкость для розжига": 0.5,
    "телефон": 0.3,
    "книга": 1,
    "кружка": 0.2
}
bp = backpack_natural(GEAR, 5)
print(f"Предметы в рюкзаке: {bp[0]} \n общий вес: {bp[1]}")
for e in backpack_all(GEAR, 2):
    print(e)
