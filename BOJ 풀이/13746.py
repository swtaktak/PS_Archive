import sys
from collections import deque
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def bfs(r, c):
    queue = deque()
    visited[r][c] = True
    queue.append((r, c))
    
    while queue:
        cr, cc = queue.popleft()
        for mv in mv_list:
            nr, nc = cr + mv[0], cc + mv[1]
            if 0 <= nr < rows and 0 <= nc < cols:
                if island[nr][nc] != 'W' and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    
input = sys.stdin.readline
# idea : L이 없으면, 무조건 W와 C이므로 정답은 0이다.
# 아닐 경우 L 판단을 해야 한다.
rows, cols = map(int, input().split())
island = []
land_list = [] # land에서 출발해야함.
visited = [[False for _ in range(cols)] for _ in range(rows)]
for r in range(rows):
    cur_row = list(str(input()).rstrip())
    for c in range(cols):
        if cur_row[c] == 'L':
            land_list.append([r, c])
    island.append(cur_row)

if len(land_list) == 0:
    print(0)
else:
    answer = 0
    for cur_l in land_list:
        cr = cur_l[0]
        cc = cur_l[1]
        if not visited[cr][cc]:
            answer += 1
            bfs(cr, cc)
    print(answer)