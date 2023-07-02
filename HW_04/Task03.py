# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
#  где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.

def dict_transform(**kwargs):
    res = {}
    for key, value in kwargs.items():
        if value.__hash__:
            res[value] = key
        else:
            res[value.__str__()] = key
    return res

print(dict_transform(a = 15, b = 5, c = "test"))