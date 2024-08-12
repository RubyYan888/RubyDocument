# func_py_find_nth_fibonacci.py
def func_py_find_nth_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(func_py_find_nth_fibonacci(10))
