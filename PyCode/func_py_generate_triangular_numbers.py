# func_py_generate_triangular_numbers.py
def func_py_generate_triangular_numbers(n):
    return [i * (i + 1) // 2 for i in range(1, n + 1)]

print(func_py_generate_triangular_numbers(10))
