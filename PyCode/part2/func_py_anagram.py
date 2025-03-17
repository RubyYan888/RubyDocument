# func_py_anagram.py

def func_py_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

def test_anagram():
    pairs = [("listen", "silent"), ("evil", "vile"), ("hello", "world")]
    for s1, s2 in pairs:
        print(f"'{s1}' and '{s2}' are anagrams: {func_py_anagram(s1, s2)}")

if __name__ == "__main__":
    test_anagram()
