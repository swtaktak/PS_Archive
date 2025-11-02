import sys
mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(cur_row, cur_col, cur_time):
    if cur_time == 0:
        return 1 if (cur_row, cur_col) == (er, ec) else 0
    
    if dp[cur_row][cur_col][cur_time] != -1:
        return dp[cur_row][cur_col][cur_time]
    
    dp[cur_row][cur_col][cur_time] = 0
    
    for mv in mv_list:
        nr, nc = cur_row + mv[0], cur_col + mv[1]
        if 0 <= nr < rows and 0 <= nc < cols and field[nr][nc] == '.':
            dp[cur_row][cur_col][cur_time] += dfs(nr, nc, cur_time - 1)
    return dp[cur_row][cur_col][cur_time]

rows, cols, goal = map(int, input().split())
field = []

for _ in range(rows):
    field.append(list(str(input().rstrip())))

sr, sc, er, ec = map(int, input().split())
sr, sc, er, ec = sr-1, sc-1, er-1, ec-1 # 위치 보정

dp = [[[-1 for _ in range(goal + 1)] for _ in range(cols)] for _ in range(rows)]

print(dfs(sr, sc, goal))