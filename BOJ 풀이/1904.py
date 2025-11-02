import sys
input = sys.stdin.readline
p = 15746
N = int(input())
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % p

print(dp[-1])