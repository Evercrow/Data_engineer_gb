# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.
import random

VOWEL_SET = ["A", "E", "I", "O", "U", "Y"]


def name_filler(f_name: str, line_num: int):
    pass
    with open(f_name, "a", encoding="UTF-8") as f:
        for _ in range(line_num):
            name = []
            for _ in range(random.randint(4, 7)):
                name.append(chr(random.randint(ord("a"), ord("z"))))
            name[random.randint(0, len(name)-1)] = random.choice(VOWEL_SET)
            f.write(f"{''.join(name).capitalize()}\n")


if __name__ == "__main__":
    name_filler("names.txt", 10)
