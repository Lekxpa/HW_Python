# Напишите функцию для транспонирования матрицы

def matrix_turn(matrix):
    for i in range(len(matrix)):
        for j in range(i, len((matrix[i]))):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

initial_matrix = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
                ]

print(*initial_matrix, sep="\n")
matrix_turn(initial_matrix)
print()
print(*initial_matrix, sep="\n")