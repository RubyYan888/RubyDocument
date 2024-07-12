# func_count_vowels.py
def func_count_vowels(string):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)

print(func_count_vowels("Hello World"))
