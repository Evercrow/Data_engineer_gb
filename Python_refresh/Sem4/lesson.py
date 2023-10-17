# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

def line_words(text: str):
    words = sorted(text.split())
    max_word_len = len(max(words, key=len))
    for number, word in enumerate(words, 1):
        print(f'{number} - {word:>{max_word_len}}')
        # print({ord(word[0])})


def get_unique_codes(text: str):
    """
    Напишите функцию, которая принимает строку текста.
    Сформируйте список с уникальными кодами Unicode каждого
    символа введённой строки отсортированный по убыванию.
    :param text:
    :return:
    """
    codes = set()
    for letter in text:
        codes.add(ord(letter))
    codes = sorted(list(codes), reverse=True)
    return codes


def get_range_code_dict(txt: str) -> dict:
    """
    Функция получает на вход строку из двух чисел через пробел.
    Сформируйте словарь, где ключом будет
    символ из Unicode, а значением —  целое число.
    Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.
    :param txt:
    :return:
    """
    nums = sorted(list(map(int, txt.split())))
    if len(nums) != 2:
        return None
    return {chr(x): x for x in range(nums[0], nums[1])}


def manual_sort_list(ls) -> list:
    """
    Функция получает на вход список чисел.
    Отсортируйте его элементы in place без использования встроенных в язык сортировок.
    Как вариант напишите сортировку пузырьком.
    Её описание есть в википедии.
    """
    for i in range(len(ls)):
        min_num = ls[i]
        min_index = i
        for j in range(i, len(ls)):
            if ls[j] < min_num:
                min_num = ls[j]
                min_index = j
        ls[i], ls[min_index] = min_num, ls[i]

    return ls

def employee_dict(ls_name: list[str],ls_wage:list[int],ls_bonus:list[float])->dict:
    """
    Функция принимает на вход три списка одинаковой длины:
    имена str, 
    ставка int, 
    премия str с указанием процентов вида «10.25%».
    Вернуть словарь с именем в качестве ключа и суммой 
    премии в качестве значения. 
    Сумма рассчитывается как ставка умноженная на процент премии.
    :return: 
    """
    return {name:wage*float(percent[:-1])/100 for name,wage,percent in zip(ls_name,ls_wage,ls_bonus)}

# def salary(names: list, salary:list, bonus: list) -> dict:
#     return {names[i]: salary[i]*(float(bonus[i][:-1])/100) for i in range(len(names))}


def sum_index(num_list:list, ind1,ind2) -> int:
    """
    Функция получает на вход список чисел и два индекса.
    Вернуть сумму чисел между между переданными индексами.
    Если индекс выходит за пределы списка, сумма считается
    до конца и/или начала списка.
    :return:
    """

    start = ind1 if 0<ind1<ind2  else 0
    end = ind2 if start<= ind2<len(num_list) else len(num_list)-1
    return  sum(num_list[start+1:end])

def empty_local_vars(end_char="s"):
    """
    Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
    Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None.
    Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
    :param end_char:
    :return:
    """
    print(globals())
    for name,val in globals().items():
        if name[-1] == end_char and name != end_char:
            globals()[name] = None
    print(globals())


def check_companies(comp: dict) -> bool:
        """
        Функция получает на вход словарь с названием компании в качестве ключа
        и списком с доходами и расходами (3-10 чисел) в качестве значения.
        Вычислите итоговую прибыль или убыток каждой компании.
        Если все компании прибыльные, верните истину, а если хотя бы одна убыточная — ложь.
        :return:
        """
        # for value in comp.values():
        #     if sum(value) < 0:
        #                 return False
        #     return True


        return all([sum(value) > 0 for value in comp.values()])


if __name__ == "__main__":
    TEST_STRING = "some random text bla bal bla :)"

    # line_words(TEST_STRING)
    # print(*get_unique_codes(TEST_STRING))
    # print(get_range_code_dict("45 56"))
    # print(manual_sort_list([3,6,1,2,2,5]))

    names = ["Tony","Anton","Albertina"]
    salary = [10000,20000,15000]
    prems = ["5%","10%","10%"]
    # print(employee_dict(names, salary,prems))
    # print(sum_index([3,6,1,2,2,5], 1, 4))
    s = 1000
    goals = "Three-fitty"
    LIMIT = 643
    # empty_local_vars()
