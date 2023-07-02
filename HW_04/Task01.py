# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s». Напишите функцию,
#  которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None. 
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def del_s_from_end(dict_values: dict):
    vars_to_change = [i for i in dict_values if len(i) > 1 and i[-1] == 's']
    for i in vars_to_change:
        dict_values[i[:-1]] = dict_values[i]
        dict_values[i] = None

a = 'Togas'
b = 'Vector'
c = 'Vegas'
d = 1234567
e = 0
f = 's'

# all_var = globals()
print(f'Исходные значения:\t{a = }\t{b = }\t{c = }\t{s = }\t{d = }\t{e = }\t{f = }\n')

dict_v = {a: }

def make_dictionary(k, l, m, n, o, p):
    for i in 
dict_v = 

del_s_from_end(dict_v)
print(f'Итоговые значения:\t{a = }\t{b = }\t{c = }\t{s = }\t{d = }\t{e = }\t')
print(f"{bb = }\n{var_ = }\n")