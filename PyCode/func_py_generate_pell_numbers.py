# func_py_generate_pell_numbers.py
def func_py_generate_pell_numbers(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(2 * sequence[i - 1] + sequence[i - 2])
    return sequence

print(func_py_generate_pell_numbers(10))
