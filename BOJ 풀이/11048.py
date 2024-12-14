import sys
input = sys.stdin.readline
rows, cols = map(int, input().split())
maps = []
for _ in range(rows):
    maps.append(list(map(int, input().split())))
dp = [[0 for _ in range(cols)] for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        if r == 0:
            if c == 0:
                dp[r][c] = maps[r][c]
            else:
                dp[r][c] = dp[r][c-1] + maps[r][c]
        else:
            if c == 0:
                dp[r][c] = dp[r-1][c] + maps[r][c]
            else:
                dp[r][c] = max(dp[r-1][c], dp[r][c-1]) + maps[r][c]
print(dp[-1][-1])