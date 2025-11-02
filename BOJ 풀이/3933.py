import sys
input = sys.stdin.readline

# dp를 먼저 구하고 답하게 하자.
dp = [[0, 0, 0, 0, 0] for _ in range(2 ** 15 + 1)]

for i in range(1, int((2 ** 15) ** 0.5) + 1):
    dp[i*i][1] = 1
    
    j = 1
    while j + i*i < 2 ** 15:
        dp[j + i*i][2] += dp[j][1]
        dp[j + i*i][3] += dp[j][2]
        dp[j + i*i][4] += dp[j][3]
        j += 1

while True:
    N = int(input())
    if N == 0:
        break
    else:
        print(sum(dp[N]))