# Напишите функцию группового переименования файлов. Она должна:
# * принимать в качестве аргумента желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# * принимать в качестве аргумента расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# * принимать в качестве аргумента расширение конечного файла.
# Шаблон переименованного файла: <original_name>_<new_name>_<position>.<new_extention>

from pathlib import Path
import random
import string
from re import findall

START, END = 4, 10
def rename_files(old_extens, new_name, new_extens):
    count = 0
    p = Path(Path.cwd())
    for file in p.iterdir():
        if file.suffix[1:] == old_extens:
            count += 1
            old_name, _ = Path(file).name.split('.')
            if len(findall('[aeiouyAEIOUY]', new_name)) > 0:
                new_name = ''.join(random.sample(string.ascii_lowercase, random.randint(START, END)))
            Path(file).rename(f'{old_name}_{new_name}_{count}.{new_extens}')
            # добавлен функционал, генерирующая псевдоимена - из задачи, которую решали на семинаре

rename_files('txt', 'new_name', 'pdf')