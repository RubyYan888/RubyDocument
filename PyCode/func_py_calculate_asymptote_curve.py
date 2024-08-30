# func_py_calculate_asymptote_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_asymptote_curve(a, points):
    t = np.linspace(-np.pi, np.pi, points)
    x = a * np.sin(t)
    y = a / (1 - np.cos(t))
    plt.plot(x, y)
    plt.title("Asymptote Curve")
    plt.show()

func_py_calculate_asymptote_curve(5, 1000)
