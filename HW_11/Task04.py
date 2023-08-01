# Создайте класс Матрица. Добавьте методы для: 
# вывода на печать, 
# проверку на равенство, 
# сложения, 
# *умножения матриц

class Matrix:
    """
        Создаем матрицы.
        Добавляем методы
        для вывода на печать,
        проверку на равенство,
        сложение,
        умножения матриц
    """

    def __init__(self, matr):
        self.matr = matr
        self.rows = len(self.matr)
        self.coloms = len(self.matr[0])

    def print_matr(self):
        """метод для вывода на печать"""
        for self.rows in self.matr:
            print(*self.rows)

    def __eq__(self, other):
        """проверка по строкам и столбцам"""
        if self.rows != other.rows or self.coloms != other.coloms:
            return False
        for i in range(self.rows):
            for j in range(self.coloms):
                if self.matr[i][j] != other.matr[i][j]:
                    return False
        return True

    def __add__(self, other):
        """метод сложения матриц
        необходимо проверить количество строк и столбцов матриц"""
        if self.rows != other.rows or self.coloms != other.coloms:
            raise ValueError('Матрицы должны быть одного размера')
        add_matr = [[None for _ in range(self.coloms)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.coloms):
                add_matr[i][j] = self.matr[i][j] + other.matr[i][j]
        return Matrix(add_matr)

    def __mul__(self, other):
        """
        метод умножения матриц
        Количество столбцов одной матрицы должно совпадать
        с количеством строк другой матрицы
        """
        if self.coloms != other.rows:
            raise ValueError('Количество столбцов одной матрицы должно совпадать с количеством строк другой матрицы')
        mult_matr = [[None for _ in range(self.coloms)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(other.coloms):
                for k in range(self.coloms):
                    mult_matr[i][j] = self.matr[i][k] * other.matr[k][j]
        return Matrix(mult_matr)

    def __str__(self):
        return f'Матрица {self.matr}'

    def __repr__(self):
        return f'Матрица: (matrix = {self.matr}, rows = {self.rows}, coloms = {self.coloms})'


matr1 = Matrix([[1, 2, 3],
                [1, 2, 3],
                [1, 2, 3]])
# print(repr(matr1))
# print(str(matr1))
matr2 = Matrix([[1, 2, 3],
                [1, 2, 3],
                [1, 2, 3]])
# print(repr(matr2))
# print(f'Сравниваем матрицы: \n{matr1 == matr2}\n')
# print('Матрица 1: ')
# matr1.print_matr()
# print('Матрица 2: ')
# matr2.print_matr()
# matr3 = matr1 + matr2
# print(f'Складываем матрицы: ')
# matr3.print_matr()
matr4 = matr1 * matr2
print(f'Умножаем матрицы: ')
matr4.print_matr()