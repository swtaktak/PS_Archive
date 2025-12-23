# 14289 행렬 사이즈가 커짐.
import sys
input = sys.stdin.readline
P = 1000000007

def mat_prod(m1, m2, P):
    result = [[0 for _ in range(vertex)] for _ in range(vertex)]
    for i in range(vertex):
        for j in range(vertex):
            for k in range(vertex):
                result[i][j] += ((m1[i][k] * m2[k][j]) % P)
    return result

def mat_mul(X, N):
    if N == 1:
        return mat
    else:
        temp = mat_mul(X, N // 2)
        if N % 2 == 0:
            return mat_prod(temp, temp, P)
        else:
            return mat_prod(mat_prod(temp, temp, P), mat, P)


vertex, edge = map(int, input().split())

mat = [[0 for _ in range(vertex)] for _ in range(vertex)]
for _ in range(edge):
    l, r = map(int, input().split())
    mat[l-1][r-1] = 1
    mat[r-1][l-1] = 1

D = int(input())

result_mat = mat_mul(mat, D)
print(result_mat[0][0] % P)