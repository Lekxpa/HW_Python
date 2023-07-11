# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел 
# для случайной расстановки ферзей в задаче выше. Проверяйте различные 
# случайные варианты и выведите 4 успешных расстановки. 
# *Выведите все успешные варианты расстановок

from random import randint
import itertools

def random_positions():
    pos = []
    while len(pos) < 8:
        rand_data = randint(0, 7), randint(0, 7)
        if rand_data not in pos:
            pos.append(rand_data)
    return pos

def check_queen_positions(positions: list):
    for row, col in positions:
        r, c = row, col
        while r < 8 or c < 8:
            if (r + 1, c + 1) in positions:
                return False
            r += 1
            c += 1
        r, c = row, col
        while 0 <= r < 8 or 0 <= c < 8:
            if (r + 1, c - 1) in positions:
                return False
            r += 1
            c -= 1
    return True

print(check_queen_positions())


def queens():
    for p in itertools.permutations(range(8)):
        yield [x for x in enumerate (p)]
for q in queens ():
    err = False
    for a, b in ((a, b) for a in q for b in q if a [0] < b [0]):
        if abs (a [0] - b [0]) == abs (a [1] - b [1]):
            err = True
            break
    if not err: print (q)