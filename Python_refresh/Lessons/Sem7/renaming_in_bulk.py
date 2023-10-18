# 2. Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6
# из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
from pathlib import Path


def renaming_func(src_ext: str, target_ext: str, target_name="", digits=2, cut_range: tuple = None):
    """
    Массовое переименовывание файлов в текущей директории
    src_ext расширение исходного файла;
    target_ext расширение конечного файла;
    опционально:
    target_name желаемое имя перед порядковым номером
    digits - количество цифр на конце имени(добивается нулями)
    cut_range - если передано, то это начало и конец среза исходного имени, для добавления в начало нового имени
    """
    file_count = 1
    cur_dir = Path.cwd()
    if src_ext[0] != '.':
        src_ext = '.' + src_ext
    if target_ext[0] != '.':
        target_ext = '.' + target_ext
    if cut_range is None:
        start_slice = 0
        stop_slice = 0
    else:
        start_slice = cut_range[0]
        stop_slice = cut_range[1]

    for file in cur_dir.iterdir():
        if file.suffix == src_ext:
            name_str = f"{file.name[start_slice:stop_slice]}{target_name}{str(file_count).zfill(digits)}{target_ext}"
            # print(name_str)
            file.replace(name_str)
            file_count += 1
