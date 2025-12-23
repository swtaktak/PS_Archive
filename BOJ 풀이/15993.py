# 15993
# 홀짝 경우 나누기
P = 1000000009

import sys
input = sys.stdin.readline

# 10만까지 한번에 계산
dp = [[0, 0] for _ in range(100001)] # 짝, 홀

# 1
dp[1] = [0, 1]
# 2, 1 + 1
dp[2] = [1, 1]
# 3, 2 + 1, 1 + 2, 1 + 1 + 1
dp[3] = [2, 2]

for i in range(4, 1000001):
    # i-3 에 다가 3을 더하는 방법
    dp[i][0] += (dp[i-3][1]) % P
    dp[i][1] += (dp[i-3][0]) % P
    
    # i-2에다가 2를 더하는 방법
    dp[i][0] += (dp[i-2][1]) % P
    dp[i][1] += (dp[i-2][0]) % P
    
    # i-1에다가 1을 더하는 방법
    dp[i][0] += (dp[i-1][1]) % P
    dp[i][1] += (dp[i-1][0]) % P
    
T = int(input())
for _ in range(T):
    N = int(input())
    print("%d %d" % (dp[N][1] % P, dp[N][0] % P))