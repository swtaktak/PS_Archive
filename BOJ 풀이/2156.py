# DP?
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N)
num_list = []

for _ in range(N):
    num_list.append(int(input()))

for i in range(N):
    if i == 0:
        dp[i] = num_list[i]
    elif i == 1:
        dp[i] = num_list[i] + num_list[i-1]
    elif i == 2:
        dp[i] = max(num_list[2] + num_list[0], num_list[2] + num_list[1], dp[1])
    else:
        # 3개 중 어느거 안 마실래?
        case_1 = dp[i-3] + num_list[i-1] + num_list[i]  # i-2번째 스킵
        case_2 = dp[i-2] + num_list[i] # i-1번째 스킵
        case_3 = dp[i-1] # i번째 스킵
        dp[i] = max(case_1, case_2, case_3)
print(dp[-1])