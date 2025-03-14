# func_py_count_words.py

def func_py_count_words(sentence):
    return len(sentence.split())

def test_count_words():
    sentences = ["Hello world", "Python is great", "I love programming"]
    for sentence in sentences:
        print(f"Word count in '{sentence}': {func_py_count_words(sentence)}")

if __name__ == "__main__":
    test_count_words()
