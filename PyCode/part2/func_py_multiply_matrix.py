# func_py_multiply_matrix.py

import numpy as np

def func_py_multiply_matrix(a, b):
    return np.dot(a, b)

def test_multiply_matrix():
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(f"Matrix product:\n{func_py_multiply_matrix(A, B)}")

if __name__ == "__main__":
    test_multiply_matrix()
