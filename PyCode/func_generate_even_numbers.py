# func_generate_even_numbers.py
def func_generate_even_numbers(n):
    return [i for i in range(n) if i % 2 == 0]

print(func_generate_even_numbers(10))
