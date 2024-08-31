# func_py_calculate_sine_wave.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_sine_wave(amplitude, frequency, points):
    t = np.linspace(0, 2 * np.pi, points)
    y = amplitude * np.sin(frequency * t)
    plt.plot(t, y)
    plt.title("Sine Wave")
    plt.show()

func_py_calculate_sine_wave(1, 5, 1000)
