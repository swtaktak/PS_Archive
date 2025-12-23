# 14722
# DP?

import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 다음에 마실 우유를 상태로 분리해야 한다.
dp = [[[-1 for _ in range(3)] for _ in range(N)] for _ in range(N)]

if graph[0][0] == 0:
    dp[0][0][1] = 1

for r in range(N):
    for c in range(N):
        if r == 0 and c == 0:
            continue
        for k in range(3):
            if r > 0 and dp[r-1][c][k] != -1:
                dp[r][c][k] = max(dp[r][c][k], dp[r-1][c][k])
            if c > 0 and dp[r][c-1][k] != -1:
                dp[r][c][k] = max(dp[r][c][k], dp[r][c-1][k])
        
        cur_milk = graph[r][c]
        if dp[r][c][cur_milk] != -1:
            next_milk = (cur_milk + 1) % 3
            dp[r][c][next_milk] = max(dp[r][c][next_milk], dp[r][c][cur_milk] + 1)
print(max(dp[-1][-1]))