# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
#  Функцию hex используйте для проверки своего результата.
# создать набор из цифр шестнадцатеричной системы или словарь

num = int(input('\nВведите число: '))
number = num
const = 16
list = []
dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
while num > 0:
    list.append(str(dict[num % const]))
    num //= const
print(f'\nРезультат: 0x{"".join(list[::-1])}\n')

print(f'Проверка результата функцией hex: {hex(number)}\n')