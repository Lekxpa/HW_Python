# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
import csv
from random import randint

rnd_start_str = 100
rnd_end_str = 1000
rnd_start_data = 1
rnd_end_data = 50

def create_file_csv(path):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['a', 'b', 'c'])
        lines = randint(rnd_start_str, rnd_end_str)
        for _ in range(lines):
            csv_writer.writerow([randint(rnd_start_data, rnd_end_data), randint(rnd_start_data, rnd_end_data), randint(rnd_start_data, rnd_end_data)])

create_file_csv('./roots.csv')