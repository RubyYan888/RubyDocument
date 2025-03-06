# func_py_sort_list_by_length.py
def func_py_sort_list_by_length(lst):
    return sorted(lst, key=len)

print(func_py_sort_list_by_length(["apple", "banana", "kiwi", "cherry"]))
