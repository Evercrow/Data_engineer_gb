# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.
import json
import csv
from pathlib import Path


def input_id_data(extension="json"):
    with open("files/id_data.json", "w", encoding="UTF-8") as f:
        groups = {str(i): list() for i in range(1, 8)}
        while True:
            user = dict()
            access = input("Введите уровень доступа(1-7): ")
            while True:
                id_ = input("Введите id: ")
                exists = False
                for u in groups[access]:
                    if id_ in u.keys():
                        print("Такой id уже есть в данной группе")
                        exists = True
                        break
                if not exists:
                    break
            user[id_] = input('Введите имя: ')
            groups[access].append(user)
            # print(groups)
            if input("Хотите выйти?") == "y":
                break
        json.dump(groups, f, indent=4)
    if extension == "csv":
        convert_to_csv(Path("files/id_data.json"))


def convert_to_csv(filepath: Path):
    with (open(filepath, "r", encoding="UTF-8") as js_f,
          open(filepath.with_suffix(".csv"), "w", encoding="UTF-8", newline="") as csv_f
          ):
        my_dict = json.load(js_f)
        csw_write = csv.writer(csv_f, dialect="excel", quoting=csv.QUOTE_NONNUMERIC)
        fieldnames = ["access", "id", "name"]
        csw_write.writerow(fieldnames)
        for access in my_dict.keys():
            if my_dict[access]:
                for user in my_dict[access]:
                    for u_id, u_name in user.items():
                        result = (u_id, u_name, access)
                        csw_write.writerow(result)


if __name__ == "__main__":
    # input_id_data("csv")
    convert_to_csv(Path("files/id_data.json"))
