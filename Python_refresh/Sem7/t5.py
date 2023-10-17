# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.
from pathlib import Path


def create_subdir(ext: str, wd: Path):
    cur_path = Path(wd) / Path(ext + "_dir")
    try :
        cur_path.mkdir()
    except FileExistsError:

        pass
    for file in wd.iterdir():
        if file.suffix == "." + ext:
            file.replace(cur_path / file.name)


if __name__ == "__main__":
    create_subdir("txt", Path("dump_dir"))
