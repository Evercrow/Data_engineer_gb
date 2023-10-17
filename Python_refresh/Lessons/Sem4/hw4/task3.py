"""
Возьмите задачу о банкомате из семинара 2:

Напишите программу банкомат.
Начальная сумма равна нулю
Допустимые действия: пополнить, снять, выйти
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%
Нельзя снять больше, чем на счёте
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
Любое действие выводит сумму денег

Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

SUM_INCREMENT = 50
COMMISSION_PERCENTAGE = 0.015
MINIMUM_CUT = 30
MAXIMUM_CUT = 600
DIVIDEND_PERIOD = 3
DIVIDEND_PERCENTAGE = 0.03
RICH_LIMIT = 5_000_000
RICH_TAX = 0.1


def rich_tax():
    global balance
    if balance > RICH_LIMIT:
        change = balance * RICH_TAX
        balance -= change
        log_change("-tax", change)


def round_to_increment(x):
    base = SUM_INCREMENT
    return base * round(x / base)


def deposit(num):
    global balance, operation_counter
    operation_counter += 1
    balance += num
    log_change("+dep", num)
    rich_tax()
    check_dividend()



def check_dividend():
    global balance, operation_counter
    if operation_counter == DIVIDEND_PERIOD:
        change = DIVIDEND_PERCENTAGE * balance
        balance += change
        log_change("+div", change)
        operation_counter = 0


def withdraw(num):
    global balance, operation_counter
    if num >= balance:
        print("Сумма выше вашего баланса недостаточна")
        rich_tax()
        return
    commission = COMMISSION_PERCENTAGE * num
    if commission < 30:
        commission = 30
    if commission > 600:
        commission = 600
    change = num + commission
    balance -= change
    log_change("-wit", change)
    operation_counter += 1
    check_dividend()


def exit_atm():
    print("Thank you for using our  ATM! Goodbye!")
    print("Operation history:")
    print(*operation_log, sep='\n')
    exit()


def show_balance():
    print(f"Текущий баланс {balance:.2f}$")


def log_change(oper_type: str, oper_sum: int):
    operation_log.append(f"{oper_type} {oper_sum}, {balance=:.2f}$")


if __name__ == "__main__":
    operation_log = []
    balance = 0
    operation_counter = 0
    print("Добро пожаловать!")
    while True:
        print("1- Пополнить\n"
              "2- Снять\n"
              "3- Просмотр баланса\n"
              "4- Выйти")
        match int(input("Введите номер меню: ").strip()):
            case 1:
                deposit(round_to_increment(int(input("Введите сумму пополнения, кратную 50: "))))
                show_balance()
            case 2:
                withdraw(round_to_increment(int(input("Введите сумму снятия, кратную 50: ").strip())))
                show_balance()
            case 3:
                show_balance()
            case 4:
                exit_atm()
            case _:
                print("ввод неопознан, повторите")

