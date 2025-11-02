import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
def bfs(r, c):
    global visited
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while q:
        cr, cc = q.popleft()
        for mv in mv_list:
            nr = cr + mv[0]
            nc = cc + mv[1]
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and grass[nr][nc] > 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))        
    
rows, cols = map(int, input().split())
grass = []
for r in range(rows):
    c = list(map(int, input().split()))
    grass.append(c)

visited = [[False for _ in range(cols)] for _ in range(rows)]

island = 0
for r in range(rows):
    for c in range(cols):
        if grass[r][c] > 0 and not visited[r][c]:
            bfs(r, c)
            island += 1
print(island)