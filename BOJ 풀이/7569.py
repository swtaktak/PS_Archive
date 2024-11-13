# 3차원 토마토 문제..
import sys
from collections import deque
input = sys.stdin.readline
cols, rows, heights = map(int, input().split())
mv_list = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
visited_box = [[[-2 for _ in range(cols)] for _ in range(rows)] for _ in range(heights)]

tomato_box = [[] for _ in range(heights)]
for i in range(heights):
    for _ in range(rows):
        cur_row = list(map(int, input().split()))
        tomato_box[i].append(cur_row)
max_date = 0

def bfs(visited_box):
    queue = deque()
    for i in range(heights):
        for j in range(rows):
            for k in range(cols):
                if tomato_box[i][j][k] == 1:
                    queue.append((i, j, k))
                    visited_box[i][j][k] = 0
                elif tomato_box[i][j][k] == -1:
                    visited_box[i][j][k] = -1
                else:
                    visited_box[i][j][k] = -2
    while queue:
        cx, cy, cz = queue.popleft()        
        for mv in mv_list:
            nx, ny, nz = cx + mv[0], cy + mv[1], cz + mv[2]
            if 0 <= nx < heights and 0 <= ny < rows and 0 <= nz < cols:
                if visited_box[nx][ny][nz] == -2:
                    visited_box[nx][ny][nz] = visited_box[cx][cy][cz] + 1
                    queue.append((nx, ny, nz))                   
    return visited_box

visited_box = bfs(visited_box)
max_date = 0
def get_answer(visited_box, max_date):
    for i in range(heights):
        for j in range(rows):
            for k in range(cols):
                if visited_box[i][j][k] == -2:
                    return -1
                else:
                    if visited_box[i][j][k] > max_date:
                        max_date = visited_box[i][j][k]
    return max_date

print(get_answer(visited_box, max_date))
                