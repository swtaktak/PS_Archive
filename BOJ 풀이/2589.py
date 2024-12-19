import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs(i, j):
    q = deque()
    visited[i][j] = 0
    q.append([i, j])
    ans_dist = 0
    while q:
        cx, cy = q.popleft()
        for mv in mv_list:
            nx, ny = cx + mv[0], cy + mv[1]
            if 0 <= nx < rows and 0 <= ny < cols:
                if visited[nx][ny] == -1 and land[nx][ny] == 'L':
                    cur_dist = visited[cx][cy] + 1
                    visited[nx][ny] = cur_dist
                    q.append([nx, ny])
                    if cur_dist > ans_dist:
                        ans_dist = cur_dist
    return ans_dist

rows, cols = map(int, input().split())
land = []
for _ in range(rows):
    cur_row = list(str(input()).rstrip())
    land.append(cur_row)
answer = 0
for i in range(rows):
    for j in range(cols):
        if land[i][j] == 'L':
            visited = [[-1 for _ in range(cols)] for _ in range(rows)]
            result = bfs(i, j)
            if result > answer:
                answer = result
print(answer)