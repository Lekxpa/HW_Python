# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её 
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle. 
# Для дочерних объектов указывайте родительскую директорию. 
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, 
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий. 
# example:
# obj,parent,obj_type,size
#  [
# {
# "obj": "data.csv",
# "parent": "HW_8",
# "obj_type": "file",
# "size": 262
# },
# obj,parent,obj_type,size
# data.csv,HW_8,file,262
# data.json,HW_8,file,1103
# data.pickle,HW_8,file,342
# result1.csv,HW_8,file,198
# result1.json,HW_8,file,406
# result1.pickle,HW_8,file,242
# task_1.py,HW_8,file,2284
# test.py,HW_8,file,3096

import os
import json
import csv
import pickle


def create_folder(dic_lst):
    if not os.path.exists('Folder_task03'):
        os.makedirs('Folder_task03')
    with(
        open('Folder_task03/data.json', 'w', encoding='utf-8') as fj,
        open('Folder_task03/data.csv', 'w', newline='', encoding='utf-8') as fcsv,
        open('Folder_task03/data.pickle', 'wb') as fp
    ):
        json.dump(dic_lst, fj, indent=2)

        csv_write = csv.DictWriter(fcsv, fieldnames=['name_obj', 'parent', 'obj_type', 'size'])
        csv_write.writeheader()
        csv_write.writerows(dic_lst)

        pickle.dump(dic_lst, fp)


def size_dir(directory):
    size_all_files = 0
    for path, directr, file in os.walk(directory):
        for f in file:
            size_all_files += os.path.getsize(os.path.join(path, f))
    return size_all_files


def save_dir_info(directory):
    dic_lst = []
    for path, directr, file in os.walk(directory):
        for i in file:
            dic_lst.append({
                'name_obj': i,
                'parent': os.path.basename(path),
                'obj_type': 'file',
                'size': os.path.getsize(os.path.join(path, i))})
        for j in directr:
            dic_lst.append({
                'name_obj': j,
                'parent': os.path.basename(path),
                'obj_type': 'directory',
                'size': size_dir(os.path.join(path, j))})
        return dic_lst


directory = os.getcwd()
create_folder(save_dir_info(directory))
