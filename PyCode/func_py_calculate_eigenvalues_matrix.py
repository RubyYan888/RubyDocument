# func_py_calculate_eigenvalues_matrix.py
import numpy as np

def func_py_calculate_eigenvalues_matrix(matrix):
    return np.linalg.eigvals(matrix)

matrix = np.array([[5, 4], [4, 5]])
print(func_py_calculate_eigenvalues_matrix(matrix))
