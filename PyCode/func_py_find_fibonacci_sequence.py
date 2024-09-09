# func_py_find_fibonacci_sequence.py
def func_py_find_fibonacci_sequence(n):
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

print(func_py_find_fibonacci_sequence(10))
