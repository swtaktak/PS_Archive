# 2086
# 피보나치 수열의 합
# Fn +.... + Fm
# sum Fm - sum Fn-1이면 되지 않나..?

import sys
input = sys.stdin.readline
P = 1000000000


def matrix_prod(m1, m2, p):
    x1 = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % p
    x2 = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % p
    x3 = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % p
    x4 = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % p
    return [[x1, x2], [x3, x4]]
def matrix_power_mod_p(matrix, n, p):
    if n == 1:
        return matrix
    else:
        temp = matrix_power_mod_p(matrix, n//2, p)
        if n % 2 == 0:
            return matrix_prod(temp, temp, p)
        else:
            return matrix_prod(matrix_prod(temp, temp, p), matrix, p)
        
matrix = [[1, 1], [1, 0]]


a, b = map(int, input().split())
large = matrix_power_mod_p(matrix, b+2, P)[0][1] - 1
small = matrix_power_mod_p(matrix, a+1, P)[0][1] - 1

print((large-small) % P)
