# fun_matrix_transpose.py
def transpose_matrix(matrix):
    return list(map(list, zip(*matrix)))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Original Matrix:")
for row in matrix:
    print(row)

transposed = transpose_matrix(matrix)
print("Transposed Matrix:")
for row in transposed:
    print(row)
