'''
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
 Функцию hex используйте для проверки своего результата.
'''


def match_hex(num: int) -> str:
    if num < 10:
        return str(num)
    match num:
        case 10:
            return "A"
        case 11:
            return "B"
        case 12:
            return "C"
        case 13:
            return "D"
        case 14:
            return "E"
        case 15:
            return "F"
        case _:
            return str(num)


u_num = int(input("Введите целое десятичное число для перевода: "))
check_num = u_num
if u_num < 0:
    SIGN = '-'
else:
    SIGN = ''
u_num = abs(u_num)

res: [str] = []
while u_num > 0:
    remainder = u_num % 16
    u_num = u_num // 16
    res.append(match_hex(remainder))

res = SIGN+'0x'+''.join(reversed(res))
print(f"Ручной метод: {res}")
print(f"Проверка через hex(): {hex(check_num)}")
