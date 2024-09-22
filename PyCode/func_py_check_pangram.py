# func_py_check_pangram.py
def func_py_check_pangram(s):
    return set("abcdefghijklmnopqrstuvwxyz").issubset(set(s.lower()))

print(func_py_check_pangram("The quick brown fox jumps over the lazy dog"))
