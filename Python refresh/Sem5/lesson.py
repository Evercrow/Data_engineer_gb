def first_gen(txt: str) -> dict:
    """
    Пользователь вводит строку из четырёх или более целых чисел, разделённых символом “/”. Сформируйте словарь, где:
    второе и третье число являются ключами
    первое число является значением для первого ключа
    четвертое и все возможные последующие числа хранятся в кортеже как значения второго ключа
    :return:
    """
    a, b, c, *d = [int(num) for num in txt.split('/')]

    d = tuple(d)

    result = {b: a, c: d}
    print(result)
    print(type(result))


def dict_from_string(txt) -> dict:
    """
    Самостоятельно сохраните в переменной строку текста.
    Создайте из строки словарь, где ключ - буква, а значение - код буквы. Напишите преобразование в одну строку.
    :return:
    """
    return {letter: ord(letter) for letter in txt}


def top_5_from_dict(mydict):
    """
    Продолжаем развивать задачу 2. Возьмите словарь, который вы получили.
    Сохраните его итератор. Далее выведите первые 5 пар ключ-значение, обращаясь к итератору, а не к словарю.
    :param mydict:
    :return:
    """
    dict_iter = iter(mydict)
    for _ in range(30):
        print(*next(dict_iter))


def sum_8_gen():
    """
    Создайте генератор чётных чисел от нуля до 100. Из последовательности исключите числа, сумма цифр которых равна 8. Решение в одну строку
    """
    # (i % 10) + (i // 10) != 8)
    return (num for num in range(0, 101, 2) if sum(map(int, str(num))) != 8)


def fizz_buzz():
    """
    Напишите программу, которая выводит на экран числа от 1 до 100.
    При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz», а вместо чисел,
    кратных пяти — слово «Buzz». Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
    Превратите решение в генераторное выражение.
    :return:
    """
    return ('FizzBuzz' if num % 15 == 0
            else 'Buzz' if num % 5 == 0
    else 'Fizz' if num % 3 == 0
    else num for num in range(1, 101))

def multiplication_table():
    """
    Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
    Таблицу создайте в виде однострочного генератора, где каждый элемент генератора - отдельный пример таблицы умножения.
    Для вывода результата используйте “принт” без перехода на новую строку.

    :return:
    """
    a = "\n"
    return (f"{num1}x{num2} = {num1*num2}{a if num2 == 9 else '' :>10}" for num1 in range(1,10) for num2 in range(1,10))

def prime_num_gen(N:int):
    """
    Создайте функцию-генератор. Функция генерирует N простых чисел, начиная с числа 2.
     Для проверки числа на простоту используйте правило:
     “число является простым, если делится нацело только на единицу и на себя”.
    :param N:
    :return:
    """

    def check_prime(num) -> bool:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    return ( i for i in range(2,N+1) if check_prime(i))





if __name__ == "__main__":

    # print(first_gen(input("Введите 4 или более чисел через символ /: ")))
    # dict2=dict_from_string("Second task check *")
    # print(dict2)
    # top_5_from_dict(dict2)
    # for i in sum_8_gen():
    #     print(i)
    # for num in fizz_buzz():
    #     print(num)
    # multi_gen = multiplication_table()
    # print(end="\t")
    # for i in multi_gen:
    #     print(i,end="\t")
        gen_prime = prime_num_gen(1000)
        print(gen_prime)
        for i in gen_prime:
            print(i)

