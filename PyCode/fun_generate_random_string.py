# fun_generate_random_string.py
import random
import string

def fun_generate_random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

print(fun_generate_random_string())
