# fun_py_sort_numbers.py

def fun_py_sort_numbers(lst):
    return sorted(lst)

def test_sort_numbers():
    numbers = [5, 1, 8, 3, 7]
    print(f"Sorted list: {fun_py_sort_numbers(numbers)}")

if __name__ == "__main__":
    test_sort_numbers()
