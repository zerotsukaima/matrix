import random
n = int(input("Введите размер матрицы: "))
m = int(input("Введите размер матрицы: "))
matrix = []

for i in range(n):
    matrix.append([])
    print("")
    for j in range(m):
        matrix[i].append(random.randint(-9, 9))
        print(matrix[i][j], end=" ")

for i in matrix:
    for j in i:
        if j % 2 == 0:
            print('\nЧетные элементы ', j)



