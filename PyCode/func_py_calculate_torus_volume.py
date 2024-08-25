# func_py_calculate_torus_volume.py
import math

def func_py_calculate_torus_volume(major_radius, minor_radius):
    return 2 * math.pi**2 * major_radius * minor_radius**2

print(func_py_calculate_torus_volume(5, 2))
