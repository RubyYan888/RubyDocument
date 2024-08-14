# func_py_find_armstrong_numbers.py
def func_py_find_armstrong_numbers(limit):
    armstrong_numbers = []
    for num in range(limit):
        digits = [int(d) for d in str(num)]
        if num == sum([d**len(digits) for d in digits]):
            armstrong_numbers.append(num)
    return armstrong_numbers

print(func_py_find_armstrong_numbers(1000))
