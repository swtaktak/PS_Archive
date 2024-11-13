import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(rows, cols, visited, tomato):
    # 방문 행렬에 경과날을 적어 볼 것이다.
    max_day = 0
    queue = deque()
    # 시작점 판단, 시작점도 바로 방문 처리 한다.
    for i in range(rows):
        for j in range(cols):
            if tomato[i][j] == 1:
                queue.append((i, j))
                visited[i][j] = 0
            elif tomato[i][j] == -1:
                visited[i][j] = -1
            else:
                # 미방문은 -2로 처리
                visited[i][j] = -2
    
    while queue:
        cur_x, cur_y = queue.popleft()
        for mv in mv_list:
            nx, ny = cur_x+mv[0], cur_y+mv[1]
            if 0 <= nx < rows and 0 <= ny < cols and visited[nx][ny] != -1:
                if visited[nx][ny] == -2:
                    visited[nx][ny] = visited[cur_x][cur_y] + 1
                    queue.append((nx, ny))
                    
    cur_date = 0
    for i in range(rows):
        for j in range(cols):
            if visited[i][j] == -2:
                return -1
            elif cur_date < visited[i][j]:
                cur_date = visited[i][j]
    return cur_date

cols, rows = map(int, input().split())
tomato = []
for i in range(rows):
    tomato.append(list(map(int, input().split())))

visited = [[0 for _ in range(cols)] for _ in range(rows)]

answer = bfs(rows, cols, visited, tomato)
print(answer)