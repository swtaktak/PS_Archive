import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
maps = []
for _ in range(rows):
    cur_row = list(str(input().rstrip()))
    cur_row = [int(x) for x in cur_row]
    maps.append(cur_row)

dp = [[0 for _ in range(cols)] for _ in range(rows)]

max_size = 0
for i in range(rows):
    for j in range(cols):
        if i == 0 or j == 0:
            if maps[i][j] == 1:
                dp[i][j] = 1
                if max_size == 0:
                    max_size = 1
            else:
                dp[i][j] = 0
        else:
            if maps[i][j] == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1]) + 1
                max_size = max(max_size, dp[i][j])
print(max_size ** 2)