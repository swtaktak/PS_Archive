import sys
input = sys.stdin.readline
dp = [1] * (251)

for i in range(1, 251):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 3
    else:
        dp[i] = dp[i-1] + 2 * dp[i-2]

while True:
    try:
        N = int(input())
        print(dp[N])
    except:
        break