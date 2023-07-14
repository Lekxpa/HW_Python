# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел 
# для случайной расстановки ферзей в задаче выше. Проверяйте различные 
# случайные варианты и выведите 4 успешных расстановки. 

from random import randint

def random_positions():
    pos = []
    while len(pos) < 8:
        rand_data = randint(0, 7), randint(0, 7)
        if rand_data not in pos:
            pos.append(rand_data)
    # print(pos)
    return pos

def check_eight_queens(pos: list):
        for row, col in pos:
            while row < 8 or col < 8:
                if (row + 1, col + 1) in pos:
                    return False
                row += 1
                col += 1
            while 0 <= row < 8 or 0 <= col < 8:
                if (row + 1, col - 1) in pos:
                    return False
                row += 1
                col -= 1
        print('Ферзи не бьют друг друга')
        print(pos)
        return True

count = 4
while count:
    result = []
    while len(result) < 1:
        tmp = check_eight_queens(random_positions())
        if tmp and tmp not in result:
            result.append(tmp)
    count -= 1
    print(*result)