# func_py_calculate_right_circular_cylinder_surface_area.py
import math

def func_py_calculate_right_circular_cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

print(func_py_calculate_right_circular_cylinder_surface_area(5, 10))
