# 17425
# Idea : double counting
import sys
input = sys.stdin.readline

MAX = 1000000
div_sum = [1 for _ in range(MAX + 1)]

for i in range(2, MAX + 1):
    for j in range(i, MAX + 1, i):
        div_sum[j] += i
        
dp = [0 for _ in range(MAX + 1)]

for i in range(1, MAX + 1):
    if i == 1:
        dp[i] = div_sum[i]
    else:
        dp[i] = dp[i-1] + div_sum[i]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])