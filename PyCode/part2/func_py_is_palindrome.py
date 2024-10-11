# func_py_is_palindrome.py
def func_py_is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
