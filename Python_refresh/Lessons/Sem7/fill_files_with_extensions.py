# Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
import random
from pathlib import Path


# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.
def create_specified_ext_files(ext: str, min_len=6, max_len=30, min_byte=256, max_byte=4096, file_quantity=42,
                               new_dir="dump_dir"):
    p = Path.cwd() / Path(new_dir)
    if not p.exists():
        p.mkdir()
    for i in range(file_quantity):
        res_file = Path(new_dir) / Path(generate_name(min_len, max_len) + ext)
        with open(res_file, "xb") as f:
            try:
                f.write(generate_name(min_byte, max_byte, bytestr=True))
            except FileExistsError:
                i -= 1


def generate_name(min_len, max_len, bytestr=False) -> bytes | str:
    name = []
    for _ in range(random.randint(min_len, max_len)):
        name.append(chr(random.randint(ord("a"), ord("z"))))

    res = ''.join(name).lower()
    if bytestr:
        return res.encode('utf-8')
    return res


# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.
def create_files_from_dict(ext_dict: dict[str:int]):
    for key, value in ext_dict.items():
        create_specified_ext_files("." + key, file_quantity=value)


if __name__ == "__main__":
    create_specified_ext_files(".pyt", file_quantity=5, new_dir="other_dir")
    create_files_from_dict({"py": 4, "txt": 3, "xyx": 5})
