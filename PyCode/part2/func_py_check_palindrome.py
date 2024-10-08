# func_py_check_palindrome.py
def func_py_check_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]
