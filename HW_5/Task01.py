# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

def file_info(file_path):
    *file_path, f_name, f_roat = file_path.replace('.', '\\').split('\\')
    file_path = '\\'.join(file_path)
    return (f'\nПуть - {path}\nИмя файла - {f_name}\nРасширение файла - {f_roat}\n')

path = 'D:\\Linux\\ulin\\Logs\\vbox.txt'

print(file_info(path))