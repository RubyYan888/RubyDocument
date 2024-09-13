# func_py_find_common_elements.py
def func_py_find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

print(func_py_find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]))
