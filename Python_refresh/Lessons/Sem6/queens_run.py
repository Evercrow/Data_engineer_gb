# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей
# на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
from queens import read as r, print_ as p, core as c

correct1 = "a2 b4 c6 d8 e3 f1 g7 h5"
incorrect_v = "a2 b2 c6 d8 e3 f1 g7 h5"
incorrect_h = "a2 b3 c6 d8 e3 f1 g7 h5"
correct2 = "a7 b5 c3 d1 e6 f8 g2 h4"
incorrect_slash = "a3 b5 c7 d1 e6 f8 g2 h4"
test = (correct1,incorrect_v,incorrect_h, correct2, incorrect_slash)
for t in test:
    tupled_coords = r.read_position_str(t)
    ar = r.fill_array(tupled_coords)
    p.print_board(ar)
    p.show_check_result(c.check_moves(tupled_coords))
    print()
