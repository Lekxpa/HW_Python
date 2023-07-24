# * Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import json
from functools import wraps


def save_res(file):
    
    def deco(func):
        result_list = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            result = {'args': args,
                    'result': res}
            result_list.append(result)
            with open(file, "w", encoding="utf-8") as fj:
                json.dump(result_list, fj, indent=2)

            return result

        return wrapper
    
    return deco