# func_py_count_vowels.py
def func_py_count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

print(func_py_count_vowels("This is a test sentence."))
