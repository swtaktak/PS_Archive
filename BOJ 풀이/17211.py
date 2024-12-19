import sys
input = sys.stdin.readline
days, mood = map(int, input().split())
hh, hs, sh, ss = map(float, input().split())
dp = [[0, 0] for _ in range(days + 1)]

def round_half_up(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)

if mood == 0:
    dp[0] = [1, 0]
else:
    dp[0] = [0, 1]

for i in range(1, days+1):
    dp[i][0] = dp[i-1][0] * hh + dp[i-1][1] * sh
    dp[i][1] = dp[i-1][0] * hs + dp[i-1][1] * ss
print(round_half_up(dp[-1][0] * 1000))
print(round_half_up(dp[-1][1] * 1000))