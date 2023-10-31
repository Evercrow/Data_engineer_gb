# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 (task_4_res.pickle)
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.
import csv
import json
from
from pathlib import Path
import pickle


def pickle_to_csv(file_str):
    file = Path(file_str)
    with (open(file, "rb") as p,
          open(file.with_suffix(".csv"), "w", encoding="UTF-8") as csv_f):
        table_object = pickle.load(p)
        dicts_inside = []
        first_fields = []
        if isinstance(table_object, list):
            first_fields.extend(table_object[0].keys())
            dicts_inside.extend(table_object)
        elif isinstance(table_object, dict):
            first_fields.extend(table_object.keys())
            dicts_inside.append(table_object)
        else:
            print(f"Cannot convert data read from {file}")
            exit(1)
        csv_wr = csv.DictWriter(csv_f, fieldnames=first_fields, dialect="excel", quoting=csv.QUOTE_NONNUMERIC)
        csv_wr.writeheader()
        csv_wr.writerows(dicts_inside)


def pickle_to_json(file_str):
    file = Path(file_str)
    old_name = file.stem
    with (open(file, "rb") as p,
          open(file.with_stem(old_name + "_copy").with_suffix(".json"), "w", encoding="UTF-8") as json_f):
        table_object = pickle.load(p)
    full_dict = {}
    if isinstance(table_object, list):
        full_dict = {key: [] for key in table_object[0].keys()}
        for dict_next in table_object:
            for field_name in dict_next.keys():
                full_dict[field_name].append(dict_next[field_name])
    elif isinstance(table_object, dict):
        full_dict = {key: [values] for key, values in table_object.items()}
    else:
        print(f"Cannot convert data read from {file}")
        exit(1)
    json.dump(full_dict, indent=2)


if __name__ == "__main__":
    pickle_to_csv("files/task_4_res.pickle")
