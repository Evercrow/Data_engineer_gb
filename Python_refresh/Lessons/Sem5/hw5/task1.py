import os
import os.path as p


def path_tupler(path_str: str) -> (str, str, str):
    """
     функция принимает на вход строку - абсолютный путь до файла.
     возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
    :return:
    """
    p_dir, file = p.split(path_str)
    extension = p.splitext(path_str)[1]
    # Если строго следовать задаче, то выдавать нужно ту же строку, но адаптированную под систему где нужно
    # dir = p.abspath(path_str)
    return p_dir, file, extension


if __name__ == "__main__":
    test_str = os.getcwd() + "\условие.md"
    test_str2 = os.get_exec_path()
    print(path_tupler(test_str))
