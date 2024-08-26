# func_py_calculate_octagonal_prism_volume.py
import math

def func_py_calculate_octagonal_prism_volume(side_length, height):
    area_base = 2 * (1 + math.sqrt(2)) * side_length**2
    return area_base * height

print(func_py_calculate_octagonal_prism_volume(3, 10))
