# 소수가 아니다.. 페르마 소정리 불가! 
import sys
input = sys.stdin.readline

def matrix_prod(m1, m2, p):
    x1 = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % p
    x2 = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % p
    x3 = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % p
    x4 = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % p
    return [[x1, x2], [x3, x4]]
def matrix_power_mod_p(matrix, n, p):
    if n == 0:
        return [[1, 0], [0, 1]]  
    elif n == 1:
        return matrix
    else:
        temp = matrix_power_mod_p(matrix, n//2, p)
        if n % 2 == 0:
            return matrix_prod(temp, temp, p)
        else:
            return matrix_prod(matrix_prod(temp, temp, p), matrix, p)


a, r, n, mod = map(int, input().split())

matrix = [[r, 0], [a, 1]]
result = matrix_power_mod_p(matrix, n, mod)
print(result[1][0] % mod)