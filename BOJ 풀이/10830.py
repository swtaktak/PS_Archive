# 행렬의 거듭제곱, N by N임에 주의
import sys
input = sys.stdin.readline

def matrix_multi(a, b):
    sized = len(a)
    result = [[0 for _ in range(sized)] for _ in range(sized)]
    
    for i in range(sized):
        for j in range(sized):
            cur_sum = 0
            for k in range(sized):
                cur_sum += (a[i][k]*b[k][j])
            result[i][j] = cur_sum % 1000
    return result

def matrix_power(matrix, n):
    if n == 1:
        for i in range(size):
            for j in range(size):
                matrix[i][j] %= 1000
        return matrix
    else:
        temp = matrix_power(matrix, n // 2)
        if n % 2 == 0:
            return matrix_multi(temp, temp)
        else:
            return matrix_multi(matrix_multi(temp, temp), matrix)

size, powers = map(int, input().split())
matrix = []
for _ in range(size):
    cur_row = list(map(int, input().split()))
    matrix.append(cur_row)
result_matrix = matrix_power(matrix, powers)

for i in range(size):
    for j in range(size):
        print(result_matrix[i][j], end = " ")
    print()