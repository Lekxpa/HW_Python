# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.gi

from fractions import Fraction

expression1 = (input('\nВведите первую дробь в формате 4/5: '))
expression2 = (input('\nВведите вторую дробь в формате 4/5: '))

lst1 = expression1.split("/")
lst2 = expression2.split("/")
a1 = int(lst1[0])
a2 = int(lst1[1])
b1 = int(lst2[0])
b2 = int(lst2[1])
# print(a1, a2, b1, b2)
if a1 == 0 or a2 == 0 or b1 == 0 or b2 == 0:
    print('Вы ввели неверное значение. Попробуйте еще раз!')

# print(lst1)
# print(lst2)

def sum_fractions(num1_1, num1_2, num2_1, num2_2):
    if num1_2 % num2_2 == 0:
        num2_res = num1_2
        num1_res = num1_1 + (num2_1 * (num1_2 / num2_2))
    elif num2_2 % num1_2 == 0:
        num2_res = num2_2
        num1_res = num2_1 + (num1_1 * (num2_2 / num1_2))
    else: 
        num1_res = (num1_1 * num2_2) + (num2_1 * num1_2)
        num2_res = num1_2 * num2_2
    print(f'\nРезультат сложения дробей: {num1_res}/{num2_res}')    
    
def multiplication_fractions(num1_1, num1_2, num2_1, num2_2):
    num1_res = num1_1 * num2_1
    num2_res = num1_2 * num2_2
    if num1_res % num2_res == 0:
        num1_res = num1_res % (num1_res / num2_res) 
        num2_res = num2_res % (num1_2 * num2_2)
    print(f'\nРезультат умножения дробей: {num1_res}/{num2_res}')

res_sum = sum_fractions(a1, a2, b1, b2)
res_mult = multiplication_fractions(a1, a2, b1, b2)


print(f'\nПроверка суммы функцией fraction: {Fraction(a1, a2) + Fraction(b1, b2)}')
print(f'\nПроверка произведения функцией fraction: {Fraction(a1, a2) * Fraction(b1, b2)}')