import re
from collections import Counter as Counter


def match_words(big_string, word_length=1) -> list:
    # задаем часть регулярного выражения, отвечающего за количество совпадений, вставляем через интерполяцию f,
    # "+" для любой длины
    if word_length == 1:
        letter_matches = '+'
    else:
        letter_matches = f'{{{word_length},}}'  # не "служебные" фигурные скобки задваиваем в f-строках
    return re.findall(rf'[^\W\d_]{letter_matches}', big_string)


# через collections.Counter
def find_popular_words_collections(text: str, top: int = 5, word_length: int = 3) -> list:
    """
    В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
    Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
    :param word_length:задаем минимальную длину слов
    :param text:
    :param top: сколько слов выдавать в итоговом рейтинге
    :return:
    """
    words = match_words(text, word_length)
    word_counter: Counter = Counter(words)
    builtin_result = word_counter.most_common(top)
    return builtin_result


# ручными циклами
def find_popular_words_manual(text: str, top: int = 5, word_length: int = 3) -> list:
    words = match_words(text, word_length)
    words_counted = dict.fromkeys(words, 0)
    for w in words:
        words_counted[w] += 1
    manual_result = [x for x in sorted(words_counted.items(), key=lambda x: x[1], reverse=True)]
    return manual_result[:top]


# [] - cоздаем свой класс символов
# ^ - исключающий знак, если первый символ класса. Далее перечисляем:
# \w альфанумерические знаки алфавита. Нам нужно делать двойное отрицание, чтобы работало в записи класса ^\W
# ^\d_ -исключаем цифры и _
# + - 1 или больше совпадений с классом.
# regex = "[^\W\d_]+"
# test_string = "A;,./>>?()*)&^*&^%&^#Bs: f.A  sad_man,cat-dog 1 203974"
# print(re.findall(regex, test_string))
BIG_TEXT_FILE = "wiki.txt"
HOW_MANY_WORDS = 10
WORD_MINIMAL_LENGTH = 4
with open(BIG_TEXT_FILE, 'rt', encoding="UTF-8") as f:
    print(find_popular_words_collections(f.read().lower(), top=HOW_MANY_WORDS, word_length=WORD_MINIMAL_LENGTH))
with open(BIG_TEXT_FILE, 'rt', encoding="UTF-8") as f:
    print(find_popular_words_collections(f.read().lower(), top=HOW_MANY_WORDS))
with open(BIG_TEXT_FILE, 'rt', encoding="UTF-8") as f:
    print(find_popular_words_manual(f.read().lower(), top=HOW_MANY_WORDS, word_length=WORD_MINIMAL_LENGTH))
