# catalan number
import sys
input = sys.stdin.readline

d, m = map(int, input().split())
d  = (d-2) // 2
dp = [0 for _ in range(d+1)]

for i in range(d + 1):
    if i == 0:
        dp[i] = 1
    else:
        cur_ans = 0
        for j in range(0, i):
            cur_ans += (dp[i-j-1]*dp[j]) % m
        dp[i] = cur_ans % m
print(dp[-1])