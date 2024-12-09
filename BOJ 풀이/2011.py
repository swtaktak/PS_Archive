import sys
input = sys.stdin.readline
D = 1000000

N = str(input().rstrip())
dp = [0] * (len(N))

for i in range(0, len(N)):
    if i == 0:
        if N[i] == '0':
            dp[-1] = 0
            break
        else:
            dp[i] = 1
    elif i == 1:
        if 10 <= int(N[0:2]) <= 26:
            dp[i] += 1  # a, b, ab 3가지
        if int(N[1]) > 0:
            dp[i] += 1
    else:
        # 0000 dlkfk
        if 10 <= int(N[i]) + 10 * int(N[i-1]) <= 26:
            dp[i] += dp[i-2]
        if int(N[i]) > 0:
            dp[i] += dp[i-1]
        dp[i] %= D
print(dp[-1])