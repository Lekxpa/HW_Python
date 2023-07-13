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

def check_eigth_queens_pos(pos: list):
    for row, col in pos:
        r, c = row, col
        while r < 8 or c < 8:
            if (r + 1, c + 1) in pos:
                return False
            r += 1
            c += 1
        r, c = row, col
        while 0 <= r < 8 or 0 <= c < 8:
            if (r + 1, c - 1) in pos:
                return False
            r += 1
            c -= 1
    return True

print(check_eigth_queens_pos(random_positions))


def queens_all_wins():
    for pos in itertools.permutations(range(8)):
        yield [x for x in enumerate(pos)]
for i in queens_all_wins():
    err = False
    for a, b in ((a, b) for a in i for b in i if a[0] < b[0]):
        if abs(a[0] - b[0]) == abs(a[1] - b[1]):
            err = True
            break
    if not err: 
        print(i)

# queens_all_wins()

# COUNT = 1
# def queens_4_var():
#     COUNT = 1
#     while COUNT <= 4:
#         # for pos in itertools.permutations(range(8)):
#         #     yield [x for x in enumerate(pos)]
#         #     break
#     # while COUNT <= 4:
#         for i in queens():
#             err = False
#             for a, b in ((a, b) for a in i for b in i if a[0] < b[0]):
#                 if abs(a[0] - b[0]) == abs(a[1] - b[1]):
#                     err = True
#                     break
#             if not err: 
#                 print(i)
#                 # COUNT += 1
#                 break

# def check_queen_4_var():
#     count = 0
#     # arrangements_queen = open('true_placement_queens.txt', 'a')
#     # arrangements_queen.write('Список координат ферзей с правильной расстановкой:\n')
#     while count <= 4:
#         rand = intersection_search(random_queens.queens_rnd_x_y())
#         if rand == 0:
#             continue
#         count += 1
        # arrangements_queen.write(f'{count} Координаты правильной расстановки - {queens_arrangements}\n')
        # arrangements_queen.close()
        
# check_eight_queens(random_positions())

