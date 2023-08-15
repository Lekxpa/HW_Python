# Напишите код, который запускается из командной строки и получает на вход путь 
# до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# * имя файла без расширения или название каталога,
# * расширение, если это файл,
# * флаг каталога,
# * название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя логирование.

import logging
import os
from collections import namedtuple


logging.basicConfig(filename='log_task01.log',
                    level=logging.INFO,
                    encoding='utf-8',
                    format='{levelname:<5} {asctime} {msg}', 
                    style='{'
                    )

Data_path = namedtuple('Data_path', ['name', 'extention', 'directory', 'parent_directory'])


def get_data_path(directory_path):
    lst = []
    for i in os.listdir(directory_path):
        path_f = os.path.join(directory_path, i)
        # p_name = os.path.dirname(directory_path)
        # p_name = os.path.dirname(os.path.dirname(directory_path))
        # parent_name = os.path.basename(p_name)[1]
        # parent_name = os.path.split(p_name)[1]
        parent_name = os.path.split(directory_path)[1]
        if os.path.isdir(path_f):
            lst.append(Data_path(i, '', True, parent_name))
            lst += get_data_path(path_f)
        else:
            name, extention = os.path.splitext(i)
            lst.append(Data_path(name, extention, False, parent_name))
    return lst

directory_path = input('укажите полный путь до директории: ')
lst = get_data_path(directory_path)
for i in lst:
    logging.info(i)

# мой путь для проверки - d:\Python\HWs\HW_Python\\HW_15