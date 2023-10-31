import os
from json import dump as j_dump
import csv
from pickle import dump as p_dump
import pickle
from typing import Iterator
from sys import argv
from pathlib import Path

EMPTY_DIR_SIZE = 0


def look_at_dir(dir_path: str):
    """
    Функиця получает на вход директорию и рекурсивно обходит её и все вложенные директории.
    Результаты обхода сохраняет  в файлы json, csv и pickle со следующей информацией:
   - Для дочерних объектов указана родительскую директорию.
   - Для каждого объекта указан файл это или директория.
   - Для файлов указан его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и
директорий.
    """
    with (
        open(os.path.join(os.getcwd(), "dir_info.json"), 'w', encoding='utf-8') as j_f,
        open(os.path.join(os.getcwd(), "dir_info.csv"), 'w', encoding='utf-8') as c_f,
        open(os.path.join(os.getcwd(), "dir_info.pickle"), 'wb') as p_f
    ):
        j_list = []
        csv_write = csv.writer(c_f, dialect="excel", quoting=csv.QUOTE_NONNUMERIC)
        fieldnames = ["name", "parent", "type", "size"]
        csv_write.writerow(fieldnames)
        for entry, f_size in recursive_scan(dir_path, EMPTY_DIR_SIZE):
            if entry.is_dir():
                type_field = "dir"
                parent_field = str(entry.parent)
                # Проверка подсчета размеров через os.walk
                # print(get_size(entry))
            # elif entry.is_symlink():
            #     type_field = "link"
            else:
                type_field = "file"
                parent_field = str(Path(entry.path).parent)
            # print(f"{entry.name}|{parent_field}|{type_field}|{f_size}\n")
            csv_write.writerow([entry.name, parent_field, type_field, f_size])
            # заполняем список словарей для json вида [ключ-индекс:{{name:},{parent:},{type:},{size:}}]
            j_list.append({k: v for k, v in zip(fieldnames, [entry.name, parent_field, type_field, f_size])})

        j_dump(j_list, j_f, indent=2)
        p_dump(j_list, p_f)


def recursive_scan(dir_path, size=EMPTY_DIR_SIZE) -> (os.DirEntry, int):
    """
    Генераторная функция для рекурсивного обхода в глубину с промежуточным подсчетом размера по папкам
    размер пустой папки задается через EMPTY_DIR_SIZE
    (сами названия папок тоже могут занимать несколько байт, обычно зависит от файловой системы)
    yield: file descriptor: os.EntryDir | Path(dir_path) , filesize:int
    """

    dir_size = size
    for entry in os.scandir(dir_path):
        if entry.is_dir(follow_symlinks=False):
            # заглядываем в генератор подпапки и суммируем размеры файлов.
            # Удаляем последний yield c общим размером папки генератора через //2
            subdir = sum(f[1] for f in recursive_scan(entry.path, EMPTY_DIR_SIZE)) // 2
            yield from recursive_scan(entry.path, EMPTY_DIR_SIZE)
            dir_size += subdir
        else:
            file_size = entry.stat().st_size
            dir_size += file_size
            yield entry, file_size
    yield Path(dir_path), dir_size


def get_size(start_path='.'):
    """
    Классический обход через os.walk(), используется для сверки
    """
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size


if __name__ == '__main__':
    p = argv[1] if len(argv) > 1 else "."
    print(f"Запуск обхода, аргумент пути в командной строке: {p}")
    look_at_dir(p)
    # p = os.DirEntry()
    # p.stat().st_size
    # print(*os.scandir(".")
    # )
    # print(os.path.realpath("files/"))
    # for e in recursive_scan("."):
    #     print(e.name,e.is_dir(),e.stat().st_size)
