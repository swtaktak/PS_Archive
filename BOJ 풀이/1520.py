import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def dfs(cx, cy):
    if cx == rows-1 and cy == cols-1:
        return 1
    
    if dp[cx][cy] >= 0:
        return dp[cx][cy]
    
    dp[cx][cy] = 0
    for mv in mv_list:
        nx, ny = cx + mv[0], cy + mv[1]
        if 0 <= nx < rows and 0 <= ny < cols:
            if road[cx][cy] > road[nx][ny]:
                dp[cx][cy] += dfs(nx, ny)
    return dp[cx][cy]

rows, cols = map(int, input().split())
road = []
for _ in range(rows):
    cur_row = list(map(int, input().split()))
    road.append(cur_row)
    
dp = [[-1 for _ in range(cols)] for _ in range(rows)]

 
print(dfs(0, 0))
