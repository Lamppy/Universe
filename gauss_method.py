import numpy as np
from numpy import array

def gauss(a, b):
    a = a.copy()
    b = b.copy()


    matrix = [[0] * (len(a) + 1) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a) + 1):
            if j == len(a):
                matrix[i][j] = b[i]
            else:
                matrix[i][j] = a[i][j]

    def forward():
        for i in range(len(a)):
            div = matrix[i][i]
            for j in range(len(matrix[i])):
                matrix[i][j] = matrix[i][j] / div
            for j in range(i + 1, len(a)):
                coef = matrix[j][i]
                for k in range(len(matrix[j])):
                    matrix[j][k] = matrix[j][k] - matrix[i][k] * coef


    def backward():
        x = np.zeros(len(b), dtype=float)
        for i in range(len(matrix) - 1, -1, -1):
            for j in range(i+1, len(matrix)):
                for k in range(len(matrix[i])):
                    matrix[i][k] = matrix[i][k] - matrix[j][k]*matrix[i][j]
        return x


    forward()
    x = backward()
    for mat in matrix:
        print(mat)
    return x

a = array([
    [1.5, 2.0, 1.5, 2.0],
    [3.0, 2.0, 4.0, 1.0],
    [1.0, 6.0, 0.0, 4],
    [2.0, 1.0, 4.0, 3]
], dtype=float)

b = array([5, 6, 7, 8], dtype=float)

'''oob_solution = solve_out_of_the_box(a, b)'''
solution = gauss(a, b)

print(solution)
'''print("Макс отклонение компоненты решения:", norm(solution-oob_solution, ord=1))'''
