# func_py_generate_centered_triangular_numbers.py
def func_py_generate_centered_triangular_numbers(n):
    return [3 * i * (i + 1) // 2 + 1 for i in range(n)]

print(func_py_generate_centered_triangular_numbers(10))
