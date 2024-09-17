# func_py_is_isogram.py
def func_py_is_isogram(s):
    return len(s) == len(set(s.lower()))

print(func_py_is_isogram("Python"))
