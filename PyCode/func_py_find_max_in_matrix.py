# func_py_find_max_in_matrix.py
def func_py_find_max_in_matrix(matrix):
    return max(max(row) for row in matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(func_py_find_max_in_matrix(matrix))
