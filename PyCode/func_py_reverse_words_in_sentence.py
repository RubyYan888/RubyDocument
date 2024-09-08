# func_py_reverse_words_in_sentence.py
def func_py_reverse_words_in_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

print(func_py_reverse_words_in_sentence("Hello world from Python"))
