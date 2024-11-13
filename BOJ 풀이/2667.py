import sys
from collections import deque
mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]
input = sys.stdin.readline
N = int(input())

def bfs(start_x, start_y, map, visited):
    queue = deque()
    queue.append((start_x, start_y))
    size = 0
    visited[start_x][start_y] = True
    
    while queue:
        cur_x, cur_y = queue.popleft()
        size += 1
        for mv in mv_list:
            nx = cur_x + mv[0]
            ny = cur_y + mv[1]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and map[nx][ny] == '1':
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return size

map = []
for i in range(N):
    map.append(str(input().rstrip()))

visited = [[False for _ in range(N)] for _ in range(N)]
danji_size = []

for i in range(N):
    for j in range(N):
        if map[i][j] == '1' and not visited[i][j]:
            sized = bfs(i, j, map, visited)
            danji_size.append(sized)

danji_size.sort()
print(len(danji_size))
for d in danji_size:
    print(d)