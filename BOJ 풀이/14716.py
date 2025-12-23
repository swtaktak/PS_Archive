import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[1, 0], [0, 1], [-1, 0], [0, -1],
           [1, 1], [1, -1], [-1, 1], [-1, -1]]

def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while q:
        cr, cc = q.popleft()

        for mv in mv_list:
            nr = cr + mv[0]
            nc = cc + mv[1]
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and maps[nr][nc] == 1:
                    visited[nr][nc] = True # 이 때 방문처리 해야, 바로 끝 처리임.
                    q.append((nr, nc))

rows, cols = map(int, input().split())
maps = []
for _ in range(rows):
    maps.append(list(map(int, input().split())))
    
visited = [[False for _ in range(cols)] for _ in range(rows)]

ans = 0
for r in range(rows):
    for c in range(cols):
        if not visited[r][c] and maps[r][c] == 1:
            bfs(r, c)
            ans += 1
print(ans)