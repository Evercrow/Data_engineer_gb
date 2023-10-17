def bonus_salaries(names: list[str], wages: list[int], bonuses: list[str]) -> dict[str, float]:
    """
    однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str, ставка int,
     премия str с указанием процентов вида “10.25%”.
    В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения
    :return:
    """
    return {name: wage * float(bonus[:-1])/100 for name, wage, bonus in zip(names, wages, bonuses)}


if __name__ == "__main__":
    test_names = ["Katya", "Masha", "Petya"]
    test_wage = [20000, 40000, 25000]
    test_percent = ["10%", "3.5%", "12.5%"]
    print(bonus_salaries(test_names, test_wage, test_percent))
