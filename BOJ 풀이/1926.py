import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(r, c):
    q = deque()
    q.append([r, c])
    visited[r][c] = 1
    cur_size = 1
    while q:
        cx, cy = q.popleft()
        for mv in mv_list:
            nx, ny = cx + mv[0], cy + mv[1]
            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx][ny] and picture[nx][ny] == 1:
                    cur_size += 1
                    visited[nx][ny] = True
                    q.append([nx, ny])
    return cur_size

rows, cols = map(int, input().split())
picture = []
for _ in range(rows):
    picture.append(list(map(int, input().split())))
    
visited = [[False for _ in range(cols)] for _ in range(rows)]
pic_size = []
pic_num = 0
for r in range(rows):
    for c in range(cols):
        if not visited[r][c] and picture[r][c] == 1:
            cur_size = bfs(r, c)
            pic_size.append(cur_size)
            pic_num += 1

if pic_num == 0:
    print(0)
    print(0)
else:
    print(pic_num)
    print(max(pic_size))