# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.


from datetime import datetime as dt
from calendar import isleap


def check_date(*params):
    date: str = _check_params(params[1:])
    day, month, year = list(map(int, date.split('.')))
    try:
        dt(day=day, month=month, year=year)
        _check_leap(year)
        return True
    except ValueError:
        return False


def _check_leap(year: int):
    if isleap(year):
        print('Високосный')
    else:
        print('Не високосный')


if __name__ == "__main__":
    print(check_date('20.11.2000'))


def _check_params(params: tuple) -> str:
    if len(params) != 3:
        raise ParameterCount("Параметров должно быть 3, используйте формат вызова:\npython date_console.py dd mm yyyy")
    return '.'.join(params)


class ParameterCount(Exception):
    pass
