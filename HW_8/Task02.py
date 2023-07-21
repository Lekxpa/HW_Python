# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
# Распечатайте его как pickle строку.

import pickle


def print_pickle_str():
    with open('pickle_up.csv', 'r', newline='', encoding='utf-8') as f:
        csv_ = ''
        for line in f:
            csv_ += line
        str = pickle.dumps(csv_)
        return  str

print(print_pickle_str())