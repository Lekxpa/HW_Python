# Возьмите 1-3 любые задачи из прошлых семинаров, 
# которые вы уже решали. Превратите функции в методы класса. 
# Задачи должны решаться через вызов методов экземпляра.


# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл

import random
import string
from re import findall


class FillInFile:
    
    def __init__(self, file_name, line_num):
        self.file_name = file_name
        self.line_num = line_num

    def fill_in_file(self):
        start, end = 4, 7
        count = 0
        with open(self.file_name, 'a', encoding='utf-8') as f:
            while count < self.line_num:
                name = ''.join(random.sample(string.ascii_lowercase, random.randint(start, end)))
                if len(findall('[aeiouyAEIOUY]', name)) > 0:
                    f.write(f"{''.join(name).capitalize()}\n")
                    count += 1


new_file = FillInFile('task02.txt', 8)
new_file.fill_in_file()