# catalan number
import sys
input = sys.stdin.readline

d, m = map(int, input().split())
dp = [[0 for _ in range(d + 1)] for _ in range(d + 1)]
for i in range(0, d + 1):
    if i == 0:
        dp[0][0] = 1
    elif i == 1:
        dp[1][0] = 1
        dp[1][1] = 1
    else:
        for j in range(0, i+1):
            if j == 0 or j == i+1:
                dp[i][j] = 1
            else:
                dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])
print((dp[(d-2)][(d-2)//2] // ((d-2)//2 + 1)) % m)