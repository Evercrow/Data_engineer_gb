# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********


rows = int(input("Введите количество рядов: "))
padding = rows
stars = 1

for _ in range(rows):
    print(" " * (padding - stars//2) + stars * "*")
    stars += 2

print()

# через метод .center
stars = 1
for _ in range(rows):
    drawn = stars * "*"
    print(drawn.center(rows*2))
    stars += 2
