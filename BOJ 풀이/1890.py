import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
    
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
for r in range(N):
    for c in range(N):
        cur_j = graph[r][c]
        if cur_j != 0:
            if 0 <= r + cur_j < N:
                dp[r + cur_j][c] += dp[r][c]
            if 0 <= c + cur_j < N:
                dp[r][c + cur_j] += dp[r][c]
print(dp[-1][-1])