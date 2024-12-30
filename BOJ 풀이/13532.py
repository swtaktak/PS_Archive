import sys
input = sys.stdin.readline
def matrix_prod(m1, m2):
    x1 = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0])
    x2 = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1])
    x3 = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0])
    x4 = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1])
    return [[x1, x2], [x3, x4]]
def matrix_power(matrix, n):
    if n == 0:
        return [[1, 0], [0, 1]]  
    elif n == 1:
        return matrix
    else:
        temp = matrix_power(matrix, n//2)
        if n % 2 == 0:
            return matrix_prod(temp, temp)
        else:
            return matrix_prod(matrix_prod(temp, temp), matrix)
matrix = [[0.5, 0.5], [1, 0]] 
N = int(input())
prod_result = matrix_power(matrix, N - 1)
