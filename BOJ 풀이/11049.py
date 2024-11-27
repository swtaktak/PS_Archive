# 행렬 곱셈 순서

import sys
input = sys.stdin.readline

N = int(input())
matrix_list = []
for _ in range(N):
    cur_row = list(map(int, input().split()))
    matrix_list.append(cur_row)

dp = [[0 for _ in range(N)] for _ in range(N)]

# 최초 이웃 두개에 대해서
for i in range(1, N):
    left = matrix_list[i-1]
    right = matrix_list[i]
    dp[i-1][i] = left[0] * right[0] * right[1]

# 2차부터 쭉 대각선 내려간다
for cnt in range(2, N):
    for i in range(0, N-cnt):
        j = i + cnt
        dp[i][j] = 2 ** 31 + 1
        # 어디를 선택해서 곱할 것인가? 그 중간을 다 보고 최소를 가져온다.
        # 그냥 위 아래만 비교하면, 이웃한 두개만 선택하는 거라, 중간을 띄어오는 거를 볼 수 없음.
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix_list[i][0] * matrix_list[k][1] * matrix_list[j][1])
print(dp[0][-1])