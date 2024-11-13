import sys
from collections import deque
mv_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def bfs(i, j, visited, maps):
    friend = 0
    queue = deque()
    queue.append((i, j))
    visited[i][j] = True
    while queue:
        cur_x, cur_y = queue.popleft()
        if maps[cur_x][cur_y] == "P":
            friend += 1
        for mv in mv_list:
            nx = cur_x + mv[0]
            ny = cur_y + mv[1]
            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx][ny] and maps[nx][ny] != "X":
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return friend

input = sys.stdin.readline
maps = []
rows, cols = map(int, input().split())
for _ in range(rows):
    maps.append(str(input().rstrip()))

for i in range(rows):
    for j in range(cols):
        if maps[i][j] == "I":
            visited = [[False for _ in range(cols)] for _ in range(rows)]
            answer = bfs(i, j, visited, maps)
if answer > 0:
    print(answer)
else:
    print("TT")