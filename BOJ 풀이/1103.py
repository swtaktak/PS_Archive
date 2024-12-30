import sys
input = sys.stdin.readline

def dfs(cx, cy, dist):
    global max_dist
    global flag
    max_dist = max(max_dist, dist)
    c = int(maps[cx][cy])
    nv_list = [[cx + c, cy],[cx, cy + c], [cx - c, cy], [cx, cy - c]]
    for nv in nv_list:
        nx, ny = nv[0], nv[1]
        if 0 <= nx < rows and 0 <= ny < cols and maps[nx][ny] != 'H' and dist + 1 > dp[nx][ny]:
            if not visited[nx][ny]:
                dp[nx][ny] = dist + 1 # 다음 위치
                visited[nx][ny] = True
                dfs(nx, ny, dist + 1)
                visited[nx][ny] = False
            else:
                flag = True
                print(-1)
                exit()
    return


rows, cols = map(int, input().split())
maps = []
for _ in range(rows):
    cur_row = list(str(input().rstrip()))
    maps.append(cur_row)

visited = [[False for _ in range(cols)] for _ in range(rows)]
dp = [[0 for _ in range(cols)] for _ in range(rows)]
max_dist = 0
flag = False

dfs(0, 0, 1)
if flag:
    print(-1)
else:
    print(max_dist)