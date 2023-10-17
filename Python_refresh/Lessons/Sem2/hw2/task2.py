'''
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей.
Для проверки своего кода используйте модуль fractions.
'''
import re
from fractions import Fraction
from math import gcd, lcm


def extract_nums(u_str) -> list:
    return list(map(int, re.findall(r'-?\d+', u_str)))


def is_positive(u_str) -> bool:
    """
    Для ручного метода отрицательность тоже можно выявить вручную через четность знака,
    тогда в extract_nums в регулярке не нужен поиск "-?"
    """
    if u_str.count('-') % 2 == 0:
        return True
    else:
        return False


def find_frac_sum(f1: [int], f2: [int]) -> str:
    numerator = f1[0] * f2[1] + f2[0] * f1[1]
    denominator = f1[1] * f2[1]
    nod = gcd(numerator, denominator)
    return str(numerator // nod) + "/" + str(denominator // nod)


def find_frac_multi(f1, f2):
    numerator = f1[0] * f2[0]
    denominator = f1[1] * f2[1]
    nod = gcd(numerator, denominator)
    return str(numerator // nod) + "/" + str(denominator // nod)


while True:
    print("Введите дроби в формате 'a/b'")
    frac1_str = input('Первая дробь: ')
    f1 = extract_nums(frac1_str)
    frac2_str = input('Вторая дробь: ')
    f2 = extract_nums(frac2_str)
    if len(f1) == 2 and len(f2) == 2:
        break
    print("Неверная запись дроби, не можем определить только один числитель и знаменатель")

print(f"Результат суммы дробей {find_frac_sum(f1, f2)}")
print(f"Результат произведения дробей {find_frac_multi(f1, f2)}")
print("----------")
print("Проверка через fraction:")
print(f"Сумма дробей: {Fraction(f1[0], f1[1]) + Fraction(f2[0], f2[1])}")
print(f"Произведение дробей: {Fraction(f1[0], f1[1]) * Fraction(f2[0], f2[1])}")
