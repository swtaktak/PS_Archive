import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
field = []
for _ in range(rows):
    cur_row = list(str(input().rstrip()))
    field.append(cur_row)

dp = [[0 for _ in range(cols)] for _ in range(rows)]
dp[0][0] = 1
for cr in range(1, rows):
    for cc in range(1, cols):
        # 이전 위치를 탐색
        for pr in range(0, cr):
            for pc in range(0, cc):
                if field[cr][cc] != field[pr][pc]:
                    dp[cr][cc] += dp[pr][pc]
print(dp[-1][-1])