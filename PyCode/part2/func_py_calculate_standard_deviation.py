# func_py_calculate_standard_deviation.py
import math

def func_py_calculate_standard_deviation(lst):
    mean = sum(lst) / len(lst)
    variance = sum([(x - mean) ** 2 for x in lst]) / len(lst)
    return math.sqrt(variance)
