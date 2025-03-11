# func_py_find_anagrams.py
from collections import Counter

def func_py_find_anagrams(word1, word2):
    return Counter(word1) == Counter(word2)

print(func_py_find_anagrams("listen", "silent"))
