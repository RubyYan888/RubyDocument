# func_py_generate_jugglers_numbers.py
def func_py_generate_jugglers_numbers(limit):
    def is_jugglers_number(n):
        while n != 1 and n != 4 and n != 16 and n != 37:
            n = sum(int(digit)**2 for digit in str(n))
        return n == 1

    return [n for n in range(1, limit + 1) if is_jugglers_number(n)]

print(func_py_generate_jugglers_numbers(100))
