# task_4.py

def transpose_matrix(matrix):
    """Транспонирует матрицу"""
    if not matrix:
        return []

    transposed = []
    for j in range(len(matrix[0])):
        new_row = []
        for i in range(len(matrix)):
            new_row.append(matrix[i][j])
        transposed.append(new_row)

    return transposed


# Основная программа
print("Транспонирование матрицы")

rows = int(input("Сколько строк: "))
cols = int(input("Сколько столбцов: "))

matrix = []
print("Вводите строки:")

for i in range(rows):
    numbers = input(f"Строка {i + 1}: ").split()
    row = [int(x) for x in numbers]
    matrix.append(row)

print("\nИсходная матрица:")
for row in matrix:
    for num in row:
        print(num, end=" ")
    print()

transposed = transpose_matrix(matrix)

print("\nТранспонированная матрица:")
for row in transposed:
    for num in row:
        print(num, end=" ")
    print()