import math
import matplotlib.pyplot as plt
ACCURACY = 20
def my_cos(x_arg):
    """Функция разложения косинуса по Тейлору"""
    x_degree = 1
    partial_sum = 0
    for temp_number in range(0, ACCURACY):
        partial_sum+= ((-1)**temp_number)*(x_degree/math.factorial(2*temp_number))
        x_degree *= x_arg**2
    return partial_sum
