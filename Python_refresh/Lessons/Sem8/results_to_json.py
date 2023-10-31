# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.
import json

# with open("files/results.txt","r", encoding="UTF-8") as f,
#     open("files/results.json","w",):

import json
from pathlib import Path


def convert_to_json(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        my_dict = {}
        print(path.parent / Path('result.json'))
        with open(path.parent / Path('result.json'), 'w', encoding='utf-8') as r:
            for line in f:
                my_dict[line.split()[0].capitalize()] = float(line.split()[1])
            json.dump(my_dict, r, indent=4)


if __name__ == "__main__":
    convert_to_json(Path("files/results.txt"))
