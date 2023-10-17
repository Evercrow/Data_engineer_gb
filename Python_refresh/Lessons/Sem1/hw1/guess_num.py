# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
from random import randint


def guess_game(lower_limit=0, upper_limit=1000, guess_limit=10) -> bool:
    answer: int = randint(lower_limit, upper_limit)
    guess_count: int = 1
    print(f"Загадано число от {lower_limit} до {upper_limit}")
    while guess_count <= guess_limit:
        guess: int = int(input("Введите вашу отгадку: "))
        if guess > answer:
            print("Меньше")
        elif guess == answer:
            print("Поздравляем, вы угадали!")
            return True
        else:
            print("Больше")
        print(f"У вас осталось {guess_limit - guess_count} попыток")
        guess_count += 1
    else:
        print("Ваши попытки закончились, вы проиграли")
        return False

