# func_py_find_lcm.py
def func_py_find_lcm(a, b):
    greater = max(a, b)
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1

print(func_py_find_lcm(12, 15))
