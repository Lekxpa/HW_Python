# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». Напишите функцию,
#  которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None. 
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def func() -> None:
    glob = globals()
    dict = {}
    for key, value in glob.items():
        if key == 's':
            continue
        if key.endswith('s'):
            dict[key[:-1]] = glob[key]
            glob[key] = None
    for key, value in dict.items():
        glob[key] = value

tadams = 'Form of max'
vector = 'Al', 'An', 'Pan'
motors = [2, 4, 6, 8]
s = 1234567

print(f'\nИсходные значения:\n{tadams = }\n{vector = }\n{motors = }\n{s = }\n')
func()
print(f'Измененные значения:\n{tadams = }\n{vector = }\n{motors = }\n{s = }\n')
print(f'Измененные переменные:\n{tadam = }\n{vector = }\n{motor = }\n{s = }\n')