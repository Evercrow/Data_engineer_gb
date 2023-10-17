from pathlib import Path
from typing import TextIO


def read_line_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text[:-1]


def convert(names: str | Path, numbers: str | Path, results: str | Path) -> None:
    with (
        open(names, 'r', encoding='utf-8') as f_names,
        open(numbers, 'r', encoding='utf-8') as f_numbers,
        open(results, 'w', encoding='utf-8') as f_results,
    ):
        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)
        for _ in range(max(len_names, len_numbers)):
            name = read_line_or_begin(f_names)
            txt_num = read_line_or_begin(f_numbers)
            num_i, num_f = txt_num.split('|')
            mult = int(num_i) * float(num_f)
            if mult < 0:
                f_results.write(f'{name.lower()} {-mult}\n')
            elif mult > 0:
                f_results.write(f'{name.upper()} {int(mult)}\n')


if __name__ == '__main__':
    convert(Path('names.txt'), Path('numbers.txt'), Path('results.txt'))