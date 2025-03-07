# func_py_extract_phone_numbers.py
import re

def func_py_extract_phone_numbers(text):
    return re.findall(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b', text)

print(func_py_extract_phone_numbers("Call me at 123-456-7890 or 987 654 3210."))
