# fun_py_reverse_string.py

def fun_py_reverse_string(s):
    return s[::-1]

def test_reverse_string():
    words = ["hello", "world", "python"]
    for word in words:
        print(f"Reverse of '{word}': {fun_py_reverse_string(word)}")

if __name__ == "__main__":
    test_reverse_string()
