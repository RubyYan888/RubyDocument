# fun_py_merge_dicts.py

def fun_py_merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

def test_merge_dicts():
    dict_a = {"a": 1, "b": 2}
    dict_b = {"c": 3, "d": 4}
    print(f"Merged dictionary: {fun_py_merge_dicts(dict_a, dict_b)}")

if __name__ == "__main__":
    test_merge_dicts()
