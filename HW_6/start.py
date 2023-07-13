from Task01 import check_eight_queens
from Task02 import random_positions
from Task02 import queens
from Task02 import queens_4_var

# check_data_1= [(1, 8), (2, 2), (3, 5), (4, 3), (5, 1), (6, 7), (7, 4), (8, 6)]
# for row, col in check_data_1:
#     row, col = row - 1, col - 1
#     check_data_1.append(row, col)
# # check_data_1 = check_data - 1
# print(check_data_1)

# пуск для первой задачи:
check_data = [(0, 7), (1, 1), (2, 4), (3, 2), (4, 0), (5, 6), (6, 3), (7, 5)]
print(f'\nДанные для задачи 1: {check_data}')
# для проверки: 
# ферзи не бьют друг друга - [(0, 7), (1, 1), (2, 4), (3, 2), (4, 0), (5, 6), (6, 3), (7, 5)]
# бьют - [(0, 6), (1, 0), (2, 4), (3, 2), (4, 0), (5, 6), (6, 3), (7, 5)]
print(check_eight_queens(check_data))
print()

# пуск для второй задачи

# count = 4
# print(f'Данные для задачи 2: {random_positions()}')

check_eight_queens(random_positions())

# queens_4_var()


# запуск задачи 2 - выбор всех успешных комбинаций
# print('Все успешные варианты расстановок: ')
# queens()