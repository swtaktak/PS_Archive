import sys
from collections import deque
mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]
def bfs(i, j, visited, field, row, col):
    queue = deque()
    visited[i][j] = True
    queue.append((i, j))
    
    while queue:
        cur_x, cur_y = queue.popleft()
        for mv in mv_list:
            nx = cur_x + mv[0]
            ny = cur_y + mv[1]
            if 0 <= nx < row and 0 <= ny < col:
                if not visited[nx][ny] and field[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    return visited

input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    col, row, baechu = map(int, input().split())
    field = [[0 for _ in range(col)] for _ in range (row)]
    
    for _ in range(baechu):
        y, x = map(int, input().split())
        field[x][y] = 1

    bachu_worm = 0
    visited = [[False for _ in range(col)] for _ in range (row)]
    
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and field[i][j] == 1:
                bachu_worm += 1
                visited = bfs(i, j, visited, field, row, col)
    print(bachu_worm)