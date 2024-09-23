# func_py_find_factors_sum.py
def func_py_find_factors_sum(n):
    return sum(i for i in range(1, n) if n % i == 0)

print(func_py_find_factors_sum(12))
