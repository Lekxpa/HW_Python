# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import sys

START_SUM = 0
START_OPERATIONS = 1
SUM_OF_WEALTH = 5_000_000
NALOG_OF_WEALTH = 10
MULTIPL = 50
MAX_CASH = 600
MIN_CASH = 30
INTEREST_FOR_CASH = 0.015
COUNT_OF_OPERATIONS = 3
INTEREST_FOR_OPERATIONS = 0.03


def check_input(message):
    while True:
        inp = int(input(message))
        if inp % MULTIPL != 0:
            print("Сумма должна быть кратна 50!")
        else:
            return inp
        

def increase(bal, op, ls_oper):
    inc = check_input("Введите сумму пополнения: ")
    if op % COUNT_OF_OPERATIONS == 0:
        bal += bal * INTEREST_FOR_OPERATIONS
    bal += inc
    ls_oper.append(op, 'пополнение', inc)
    op += 1
    bal = check_rich(bal, op, ls_oper)
    return bal, op


def decrease(bal, op, ls_oper):
    bal = check_rich(bal, op, ls_oper)
    dec = check_input('Введите сумму снятия: ')
    percent = dec * INTEREST_FOR_CASH
    if percent < MIN_CASH:
        percent = MIN_CASH
    elif percent > MAX_CASH:
        percent = MAX_CASH
    dec_percent = dec + percent
    if bal > dec_percent:
        bal -= dec_percent
    else:
        print("Недостаточно средств!")

    if op % COUNT_OF_OPERATIONS == 0:
        bal += bal * INTEREST_FOR_OPERATIONS
    ls_oper.append((op, 'Снятие', dec))
    ls_oper.append((op, 'Комиссия за снятие: '))
    op += 1
    return bal, op

def check_rich(bal, op, ls_oper):
    if bal > SUM_OF_WEALTH:
        nalog = (bal - SUM_OF_WEALTH) // NALOG_OF_WEALTH
        ls_oper.append((op, 'Налог на богатство', nalog))
        bal -= nalog
    return bal

def start():
    balance = START_SUM
    operations = START_OPERATIONS
    lst = []
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
                balance, operations = increase(balance, operations, lst)
            case 2:
                balance, operations = decrease(balance, operations, lst)
            case 3:
                print('Все операции: ', *lst, sep='\n')
                sys.exit()
            case _:
                print("Повторите попытку")

start()