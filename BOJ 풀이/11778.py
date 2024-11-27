def gcd(n, m):
    while m > 0:
        n, m = m, n%m
    return n

# 행렬 제곱
p = 1000000007
n, m = map(int, input().split())

gcd_nm = gcd(n, m)
# 1 1
# 1 0   이 행렬의 n승을 구현해야함.
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
result_matrix = matrix_power_mod_p(matrix, gcd_nm, p)
print(result_matrix[0][1] % p)
