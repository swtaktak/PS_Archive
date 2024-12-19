# [[4, -1], [1, 0]]
# 행렬 제곱

def matrix_prod(m1, m2, p):
    x1 = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % p
    x2 = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % p
    x3 = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % p
    x4 = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % p
    return [[x1, x2], [x3, x4]]
def matrix_power_mod_p(matrix, n, p):
    if n == 1:
        return matrix
    elif n == 0:
        return [[1, 0], [0, 1]]
    else:
        temp = matrix_power_mod_p(matrix, n//2, p)
        if n % 2 == 0:
            return matrix_prod(temp, temp, p)
        else:
            return matrix_prod(matrix_prod(temp, temp, p), matrix, p)
        
matrix = [[4, -1], [1, 0]]
p = 1000000007
n = int(input())
if n % 2 != 0:
    print(0)
else:
    n = n // 2
    result_matrix = matrix_power_mod_p(matrix, n-1, p)
    answer = (result_matrix[0][0] * 3 + result_matrix[0][1]) % p
    print(answer)

