# func_py_calculate_ellipsoid_volume.py
import math

def func_py_calculate_ellipsoid_volume(radius1, radius2, radius3):
    return (4/3) * math.pi * radius1 * radius2 * radius3

print(func_py_calculate_ellipsoid_volume(3, 4, 5))
