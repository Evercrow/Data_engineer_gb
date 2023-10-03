def find_duplicates(mix: list) -> list:
    """
    Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
    :return:
    """
    copies = set()
    uniques = set()
    for item in mix:
        if item not in uniques:
            uniques.add(item)
        else:
            copies.add(item)

    return list(copies)


test1 = [5, 1, 5, 3, 4, 15, 10, 10, 2, 241, 15]
test2 = ["word", "price", "a", 5, 5, "b", "a", "word"]
print(find_duplicates(test1))
print(find_duplicates(test2))
