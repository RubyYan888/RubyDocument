# func_py_find_evil_numbers.py
def func_py_find_evil_numbers(limit):
    return [n for n in range(1, limit) if bin(n).count('1') % 2 == 0]

print(func_py_find_evil_numbers(100))
