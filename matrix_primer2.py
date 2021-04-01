import random
n = int(input("Введите размер матрицы: "))
m = int(input("Введите размер матрицы: "))
matrix = []

for i in range(n):
    matrix.append([])
    matrix.append([])
    matrix.append([])
    print("")
    matrix[0].append(random.randint(-9, 9))
    matrix[0].append(random.randint(-9, 9))
    matrix[1].append(random.randint(-9, 9))
    matrix[2].append(random.randint(-9, 9))
    matrix[2].append(random.randint(-9, 9))
    matrix[2].append(random.randint(-9, 9))
    matrix[2].append(random.randint(-9, 9))

print(matrix, end=" ")

for i in matrix:
    for j in i:
        if j % 2 == 0:
            print('\nЧетные элементы ', j)



