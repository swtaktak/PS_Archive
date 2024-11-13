import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def bfs(cur_r, cur_c, visited, maps):
    queue = deque()
    queue.append((cur_r, cur_c))
    visited[cur_r][cur_c] = True
    cur_color = maps[cur_r][cur_c]
    
    while queue:
        cx, cy = queue.popleft()
        for mv in mv_list:
            nx = cx + mv[0]
            ny = cy + mv[1]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and maps[nx][ny] == cur_color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return visited

N = int(input())
color_map = []
blind_map = []
color_visited = [[False for _ in range(N)] for _ in range(N)]
blind_visited = [[False for _ in range(N)] for _ in range(N)]
color_cnt = 0
blind_cnt = 0

for _ in range(N):
    cur_line = str(input().rstrip())
    color_map.append(cur_line)
    blind_line = cur_line.replace('R', 'G')
    blind_map.append(blind_line)
    
for i in range(N):
    for j in range(N):
        if not color_visited[i][j]:
            color_cnt += 1
            color_visited = bfs(i, j, color_visited, color_map)
            
for i in range(N):
    for j in range(N):
        if not blind_visited[i][j]:
            blind_cnt += 1
            blind_visited = bfs(i, j, blind_visited, blind_map)

print("%d %d" %(color_cnt, blind_cnt))