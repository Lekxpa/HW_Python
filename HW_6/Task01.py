# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код,
# решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно расставить 8 ферзей так,
# чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите,
# есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

# def check_eight_queens(pos: list):
#     for row, col in pos:
#         r, c = row, col
#         while r < 8 or c < 8:
#             if (r + 1, c + 1) in pos:
#                 print('Ферзи бьют друг друга')
#                 return False
#             r += 1
#             c += 1
#         r, c = row, col
#         while 0 <= r < 8 or 0 <= c < 8:
#             if (r + 1, c - 1) in pos:
#                 print('Ферзи бьют друг друга')
#                 return False
#             r += 1
#             c -= 1
#     print('Ферзи не бьют друг друга')
#     return True


def check_eight_queens(pos: list):
    for row, col in pos:
        r, c = row, col
        while r <= 8 or c <= 8:
            if (r + 1, c + 1) in pos:
                print('Ферзи бьют друг друга')
                return False
            r += 1
            c += 1
        r, c = row, col
        while 1 <= r <= 8 or 1 <= c <= 8:
            if (r + 1, c - 1) in pos:
                print('Ферзи бьют друг друга')
                return False
            r += 1
            c -= 1
    print('Ферзи не бьют друг друга')
    return True