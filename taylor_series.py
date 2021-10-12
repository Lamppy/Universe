import math
accuracy = 20

def my_cos(x):

    x_degree = 1
    multiplier = 1
    partial_sum = 1

    for n in range(2, accuracy):

        x_degree *= x**2  
        multiplier *= ((-1)**(n-1))/(math.factorial((2*n-2)))
        partial_sum += x_degree * multiplier  

    return partial_sum

if __name__ == "__main__":
    x = float(input())
    print(my_cos(x))
