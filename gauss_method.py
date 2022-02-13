import numpy as np
from numpy import array
from numpy.ma import concatenate


def gauss(a, b):
    a = a.copy()
    b = b.copy()

    matrix = concatenate((a, array([b]).T), axis=1)

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
        for i in range(len(matrix) - 2, -1, -1):
            line = matrix[i]
            for j in range(i+1, len(matrix)):
                next_line = matrix[j]
                coef = line[j]
                for k in range(len(line)):
                    line[k] = line[k] - next_line[k]*coef
            matrix[i] = line
        x = matrix[:, -1]
        return x


    forward()
    x = backward()
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
