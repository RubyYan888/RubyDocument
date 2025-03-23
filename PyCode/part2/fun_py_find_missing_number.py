# fun_py_find_missing_number.py

def fun_py_find_missing_number(lst):
    n = len(lst) + 1
    return n * (n + 1) // 2 - sum(lst)

def test_find_missing_number():
    numbers = [1, 2, 3, 4, 6]
    print(f"Missing number: {fun_py_find_missing_number(numbers)}")

if __name__ == "__main__":
    test_find_missing_number()
