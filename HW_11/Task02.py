# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

# Создайте класс Архив, который хранит пару свойств. Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее созданных экземпляров
# сохраняются в пару списков-архивов
# list-архивы также являются свойствами экземпляра

class Archive:
    """Создаем класс Архив"""
    _instance = None
    # lst_arch = []

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.lst_arch = []
        else:
            cls._instance.lst_arch.append((cls._instance.number, cls._instance.arc_string))
            # cls._instance.lst_arch.append(args)
        return cls._instance

    def __init__(self, number, arc_string):
        self.number = number
        self.arc_string = arc_string
        # self.lst_arch.append([number, art_string])

    def __str__(self):
        return f'{self.number}, {self.arc_string}, {self.lst_arch}'

    def __repr__(self):
        return f'Arch({self.number}, "{self.arc_string}")'

# type(self).__name__

u_1 = Archive(4, "jklj")
print(u_1)
u_2 = Archive(3, "piopi")
print(u_2)
print(repr(u_2))
print(f'Документация класса: {Archive.__doc__}')

#
#     def __new__(cls, *args):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.arch_num = []
#             cls._instance.arch_string = []
#         else:
#             cls._instance.arch_num.append(cls._instance.number)
#             cls._instance.arch_string.append(cls._instance.string)
#         return cls._instance
#
#     def __init__(self, number, string):
#         self.number = number
#         self.string = string
#
#     def __str__(self):
#         return f'{self.number}, {self.string}, {self.arch_num}, {self.arch_string}'
#
# ar_1 = Archive(1, 'one')
# print(ar_1.__dict__)
# ar_2 = Archive(2, 'two')
# print(ar_2.__dict__)
# print(ar_1 is ar_2)
# print(f'Number archive: {ar_1.arch_num}')
# print(f'Strint archive: {ar_2.arch_string}')