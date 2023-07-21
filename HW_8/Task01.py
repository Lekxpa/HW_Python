# Напишите функцию, которая преобразует pickle файл хранящий список словарей 
# в табличный csv файл. Для тестированию возьмите pickle версию файла из предыдущей задачи. 
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import csv
import pickle

def from_pickle_to_csv(file_pickle, file_csv):
    with(
        open(file_pickle, 'rb') as f,
        open(file_csv, 'w', newline='', encoding='utf-8') as f_res,
    ):
        lst = pickle.load(f)
        headers = lst[0].keys()
        csv_file = csv.DictWriter(f_res, fieldnames=headers)
        csv_file.writeheader()
        csv_file.writerows(lst)

from_pickle_to_csv('task04.pickle', 'pickle_up.csv')