# func_py_calculate_dodecahedron_volume.py
import math

def func_py_calculate_dodecahedron_volume(side_length):
    return (15 + 7 * math.sqrt(5)) / 4 * side_length**3

print(func_py_calculate_dodecahedron_volume(3))
