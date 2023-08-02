# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

import time

class MyStr(str):
    """
    Создаем класс Моя Строка, в котором доступны все возможности str,
    дополнительно храним имя автора строки и время создания
    Методы: __str__
    """

    # def __init__(self, name, start_time):
    #     self.name = name
    #     self.start_time = start_time

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.start_time = time.time()
        return instance

    def __str__(self):
        return str({'value': self} | self.__dict__)
    
    def __repr__(self):
        return f'MyStr({self.name, self.start_time})'


str_1 = MyStr(5, 'Alex')
print(str_1)
print(repr(str_1))
# str_2 = MyStr('Second')
# print(str_2)
print(f'Документация класса: {MyStr.__doc__}')