# 역으로 목표지점에서 출발하여 칸 수를 구하시오!
# 갈 수 없다면, 0을 넣어야 한다.
import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def bfs(s_x, s_y, maps, dist):
    queue = deque()
    queue.append((s_x, s_y))
    dist[s_x][s_y] = 0
    
    while queue:
        cur_x, cur_y = queue.popleft()
        for mv in mv_list:
            nx = cur_x + mv[0]
            ny = cur_y + mv[1]
            if 0 <= nx < row and 0 <= ny < col:
                if maps[nx][ny] == 1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[cur_x][cur_y] + 1
                    queue.append((nx, ny))
    return dist

row, col = map(int, input().split())
maps = []
for i in range(row):
    maps.append(list(map(int, input().split())))
# visited 대신 거리 행렬을 바로 쓰자.
dist = [[-1 for _ in range(col)] for _ in range(row)]    
for i in range(row):
    for j in range(col):
        if maps[i][j] == 2:
            dist = bfs(i, j, maps, dist)

for i in range(row):
    for j in range(col):
        if maps[i][j] == 0 and dist[i][j] == -1:
            print(0, end = " ")
        elif maps[i][j] == 1 and dist[i][j] == -1:
            print(-1, end = " ")
        else:
            print(dist[i][j], end = " ")
    print()