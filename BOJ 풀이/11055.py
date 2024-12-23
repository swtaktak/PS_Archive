import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
dp = [0] * N
for i in range(N):
    if i == 0:
        dp[i] = num_list[i]
    else:
        dp[i] = num_list[i]
        for j in range(0, i):
            if num_list[j] < num_list[i]:
                dp[i] = max(dp[i], dp[j] + num_list[i])
print(max(dp))