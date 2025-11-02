# DP 문제
import sys
input = sys.stdin.readline
P = 1000000007
change_cnt = int(input())
s = str(input().rstrip())

dp = [[0 for _ in range(change_cnt + 1)] for _ in range(len(s) + 1)]
dp[0][0] = 1
for i in range(1, len(s) + 1):
    sum = 0
    for j in range(change_cnt + 1):
        sum = (sum + dp[i-1][j]) % P
        
        if j > 25:
            sum = (sum - dp[i-1][j - 26]) % P
    
        dp[i][j] = sum
print(dp[-1][-1])