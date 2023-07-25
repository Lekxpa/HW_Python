# * Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.

import csv
from functools import wraps

def finde_root(file):

    def deco(func):
        res = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(file, 'r', newline='', encoding='utf-8') as f:
                csv_read = csv.reader(f)
                next(csv_read)
                for line in csv_read:
                    args = map(int, line)
                    res.append(func(*args, **kwargs))
            return res
        
        return wrapper

    return deco