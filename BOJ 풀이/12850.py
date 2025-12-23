# 12850
# 정보과학관 -> 정보과학관

P = 1000000007

def mat_prod(m1, m2, P):
    result = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
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

mat = [
    [0, 1, 0, 1, 0, 0, 0, 0], #정보과학관
    [1, 0, 1, 1, 0, 0, 0, 0], #전산관
    [0, 1, 0, 1, 1, 1, 0, 0], #신양관
    [1, 1, 1, 0, 0, 1, 0, 0], #미래관
    [0, 0, 1, 0, 0, 1, 1, 0], #진리관
    [0, 0, 1, 1, 1, 0, 0, 1], #한경직기념관
    [0, 0, 0, 0, 1, 0, 0, 1], #학생회관
    [0, 0, 0, 0, 0, 1, 1, 0] #형남공학관
]

D = int(input())

result_mat = mat_mul(mat, D)
print(result_mat[0][0] % P)