"""Добавление некоторых арифметических функций и возможности построения графика"""
import math
import matplotlib.pyplot as plt
import numpy as np

from func_for_taylor import my_cos


if __name__=='__main__':
    angles = np.arange(-10, 10, 0.01)
    plt.plot(angles, [math.cos(x_arg) for x_arg in angles])
    plt.plot(angles, [my_cos(x_arg) for x_arg in angles])
    plt.show()
    
