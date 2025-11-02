# idea : 0번에서 툭 툭 툭 툭 치면 횟수를 낭비 가능하다!
# 따라서 최소 횟수만 보면 된다!
import sys
input = sys.stdin.readline
INF = 1000001


stair, step = map(int, input().split())

dp = [INF] * (stair + 1)
dp[0] = 0

for i in range(0, stair + 1):
    if i + 1 <= stair:
        dp[i + 1] = min(dp[i] + 1, dp[i + 1])
    
    if i + (i // 2) <= stair:
        dp[i + (i // 2)] = min(dp[i] + 1, dp[i + (i // 2)])

if dp[-1] <= step:
    print('minigimbob')
else:
    print('water')