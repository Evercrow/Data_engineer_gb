import csv
import json
from pathlib import Path


def csv_to_json(file_to_read, file_to_write):
    """
    Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
    Дополните id до 10 цифр незначащими нулями.
    В именах первую букву сделайте прописной.
    Добавьте поле хеш на основе имени и идентификатора.
    Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
    Имя исходного и конечного файлов передавайте как аргументы функции.
    :return:
    """
    with open(Path(file_to_read), 'r', encoding='utf-8') as f:
        csv_unique = csv.reader(f, dialect='excel')
        headers = csv.Sniffer().has_header(f.read(200))
        f.seek(0)
        with open(Path(file_to_write), 'w', encoding='utf-8') as r:
            all_data = []
            for i, line in enumerate(csv_unique):
                if not headers or i != 0:
                    u_id, name, access = line
                    temp = {hash(f'{name}_{u_id}'): [f'{u_id.zfill(10)}', name.capitalize(), int(access)]}
                    # чтобы корректно потом считывалось, вместо отдельных словарей, общий список кинем в файл
                    # json.dump(temp, r, indent=4)
                    all_data.append(temp)
            json.dump(all_data, r, indent=4)


if __name__ == "__main__":
    csv_to_json('files/id_data.csv', 'files/task_4_res.json')
