# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    """
        Дорабатываем класс Прямоугольник - добавляем 
        возможность сложения и вычитания
        Создается новый экземпляр  
    """

    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width else length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def square(self):
        return self.width * self.length

    def __add__(self, other):
        return self.perimeter() + other.perimeter()

    def __sub__(self, other):
        sub = self.perimeter() - other.perimeter()
        if sub < 0:
            return f'Отрицательное значение'
        return sub

    def __eq__(self, other):
        return self.square() == other.squqre()

    def __ne__(self, other):
        return self.square() != other.squqre()

    def __lt__(self, other):
        return self.square() < other.squqre()

    def __le__(self, other):
        return self.square() <= other.squqre()

    def __gt__(self, other):
        return self.square() > other.squqre()

    def __ge__(self, other):
        return self.square() >= other.square()
    
    def __str__(self):
        return f'{self.length}, {self.width}'

    def __repr__(self):
        return f'({self.length}, "{self.width}")'


    # def __ge__(self, other):
    #     return self.square() >= other.square()
    #
    # def __gt__(self, other):
    #     return self.square() > other.square()

    # def __eq__(self, other):
    #     return self.square() == other.square()

if __name__ == '__main__':
    a = Rectangle(5)
    b = Rectangle(5, 2)
    print(f'Документация класса: {Rectangle.__doc__}')
