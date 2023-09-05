# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
GUESS_LIMIT = 10
answer: int = randint(LOWER_LIMIT, UPPER_LIMIT)
guess_count: int = 1
while guess_count <= GUESS_LIMIT:
    guess: int = int(input("Введите вашу отгадку: "))
    if guess > answer:
        print("Меньше")
    elif guess == answer:
        print("Поздравляем, вы угадали!")
        break
    else:
        print("Больше")
    print(f"У вас осталось {10-guess_count} попыток")
    guess_count += 1
else:
    print("Ваши попытки закончились, вы проиграли")


