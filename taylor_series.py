"""Добавление некоторых арифметических функций и возможности построения графика"""
import math
import numpy as np
import matplotlib.pyplot as plt 



ACCURACY=20

def my_cos(*x_arg):
    """Функция разложения косинуса по Тейлору"""
    x_degree=1
    multiplier=1
    partial_sum = 1
    for temp_number in range(2,ACCURACY):      
        x_degree*=x_arg**2  
        multiplier*=((-1))/(math.factorial((2*temp_number-2)))
        partial_sum+=x_degree*multiplier  
        return partial_sum
if __name__ == '__mane__':    

    vs = np.vectorize(my_cos)
    print(my_cos, vs)
    x = np.arange(-10,10,0.1)
    angles = np.r_[-16.25:16.25:0.01]
    plt.plot(x, my_cos(x))
    plt.plot(angles, np.cos(angles))
    plt.plot(angles, vs(angles))
    plt.show()