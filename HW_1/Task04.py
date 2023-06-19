# 5. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать 
# «больше» или «меньше» после каждой попытки. Для генерации случайного числа используйте код:

# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint

num = randint(0, 1000)
tryings = 10
print('\nКомпьютер загадал число от 0 до 1000. Попробуйте его угадать! \n')

while tryings > 0:
    num_of_user = int(input('Введите число: '))
    tryings -= 1
    if num > num_of_user:
        print(f'Больше! Еще {tryings} попыток')
    elif num < num_of_user:
        print(f'Меньше!  Еще {tryings} попыток')
    else: 
        print('Ура! Угадали!!! Число ', num)
        break
else:
    print(f'Не угадали. Компьютер загадал число  {num}. Попробуйте еще раз!')
