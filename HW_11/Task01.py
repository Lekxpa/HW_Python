# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

import time

class MyStr(str):

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


str_1 = MyStr(5, 'Alex')
print(str_1)
# str_2 = MyStr('Second')
# print(str_2)