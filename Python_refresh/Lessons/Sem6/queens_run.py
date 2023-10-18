# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
# на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей
# в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки
from queens import coordinates as r, print_ as p, core as c

correct1 = "a2 b4 c6 d8 e3 f1 g7 h5"
incorrect_v = "a2 b2 c6 d8 e3 f1 g7 h5"
incorrect_h = "a2 b3 c6 d8 e3 f1 g7 h5"
correct2 = "a7 b5 c3 d1 e6 f8 g2 h4"
incorrect_bslash = "a8 b5 c7 d1 e3 f8 g2 h4"

print("Проверка входных пар в виде строки шахматных позиций")
test = (correct1, incorrect_v, incorrect_h, correct2, incorrect_bslash)
converted = []
for t in test:
    converted.append(r.read_position_str(t))
c.test_and_show_combinations(converted)
print("--------")

#  Если создавать сразу 8 любых ферзей, вероятность получить удачную комбинацию на доске в 8х8 исчезающе мала,
#  меньше миллионной процента. Поэтому для быстроты будем генерить только 4 ферзя,
#  а полные комбинации найдем через поиск удачных позиций
COMBINATIONS_TO_FIND = 4
QUEEN_AMOUNT = 4
print("Генерация любых 4-х ферзей")
counter = 0
while counter < COMBINATIONS_TO_FIND:
    new_combo = tuple(c.generate_any_queen() for _ in range(QUEEN_AMOUNT))  # генерируем случайный набор ферзей
    if c.test_queen_combo(new_combo):
        counter += 1
        print(r.index_to_str(new_combo))
        p.print_combo(new_combo)
print(f"Найдено {COMBINATIONS_TO_FIND} успешных комбинаций\n")
