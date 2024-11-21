import sys
input = sys.stdin.readline

N = int(input())
dp = [[-1 for _ in range(N)] for _ in range(N)]
num_list = list(map(int, input().split()))

# step by step
# 1글자일 경우 무조건
for i in range(N):
    dp[i][i] = 1
# 2글자일 경우
for i in range(1, N):
    if num_list[i] == num_list[i-1]:
        dp[i-1][i] = 1
    else:
        dp[i-1][i] = 0
        
for cnt in range(3, N+1):
    for i in range(N- cnt + 1):
        j = i + cnt - 1
        if num_list[i] == num_list[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = 0
        
q_num = int(input())
for _ in range(q_num):
    i, j = map(int, input().split())
    print(dp[i-1][j-1])