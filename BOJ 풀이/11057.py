import sys
input = sys.stdin.readline
p = 10007
N = int(input())

dp = [[0 for _ in range(0, 10)] for _ in range(N+1)]

for i in range(1, N+1):
    if i == 1:
        for j in range(0, 10):
            dp[i][j] = 1
    else:
        for j in range(0, 10):
            dp[i][j] = sum(dp[i-1][:j+1]) % 10007
            
answer = 0
for i in range(0, 10):
    answer += dp[N][i]
print(answer % 10007)