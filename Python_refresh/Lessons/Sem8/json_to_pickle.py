import json
import pickle
from pathlib import Path


def json_to_pickle(dir_path):
    """
    Функция ищет json файлы в указанной директории и сохраняет их содержимое в виде одноимённых
    pickle файлов
    """
    wd = Path(__file__).cwd() / Path(dir_path)
    for file in wd.rglob("*.json"):
        with (open(file, 'r', encoding='utf-8') as j,
              open(Path(file).with_suffix(".pickle"), "wb") as p):
            print(j)
            j_dict = json.load(j)
            pickle.dump(j_dict, p)


if __name__ == "__main__":
    json_to_pickle("files")
