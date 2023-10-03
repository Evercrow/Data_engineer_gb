import typing


def invert_kwargs_dict(**kwargs):
    """
    Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
    где ключ — значение переданного аргумента, а значение — имя аргумента.
    Если ключ не хешируем, используйте его строковое представление.
    """
    return {(value if isinstance(value, typing.Hashable) else " ".join(map(str, value))) : key for key,value in kwargs.items()}
# особенности тернарного оператора - работает только с одной переменной, поэтому его нужно изолировать в () от пары
# ключ:значение в dict comprehension

# test_hash = [40,"any_string",[3,5]]
# print([isinstance(e, typing.Hashable) for e in test_hash])

print(invert_kwargs_dict(first=40, second="thirty", third=["20", "and", 10]))
