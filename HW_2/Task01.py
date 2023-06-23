# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег
# задача оформлена по результатам семинара

import sys

START_SUM = 0
START_OPERATIONS = 1

def check_input(message):
    while True:
        inp = int(input(message))
        if inp % 50 != 0:
            print("Недопустимая сумма. Сумма должна быть кратна 50!")
        else:
            return inp

def increase(bal, op):
    inc = check_input("Введите количество для пополнения: ")
    if op % 3 == 0:
        bal += bal * 0.03
    bal += inc
    op += 1
    if bal > 5_000_000:
        bal -= bal // 10
    return bal, op

def decrease(bal, op):
    if bal > 5_000_000:
        bal -= bal // 10
    dec = check_input("Введите количество для снятия: ")
    percent = dec * 0.015
    if percent < 30:
        percent = 30
    elif percent > 600:
        percent = 600
    dec += percent
    if bal > dec:
        bal -= dec
    else:
        print("Недостаточно средств!")
    if op % 3 == 0:
        bal += bal * 0.03
    op += 1
    return bal, op

def start():
    balance = START_SUM
    operations = START_OPERATIONS
    while True:
        select = int(input(f"""Баланс: {balance}
Операции со счётом: {operations - 1}
    
Доступные действия:
1. Пополнить
2. Снять
3. Выход

Выберите действие: """))
        match select:
            case 1:
                balance, operations = increase(balance, operations)
            case 2:
                balance, operations = decrease(balance, operations)
            case 3:
                sys.exit()
            case _:
                print("Повторите попытку")

start()