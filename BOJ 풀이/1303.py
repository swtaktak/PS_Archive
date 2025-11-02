import sys
from collections import deque
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append([r, c])
    visited[r][c] = True
    cur_pow = 1
    cur_color = wars[r][c]
    
    while q:
        cr, cc = q.popleft()
        for mv in mv_list:
            nr, nc = cr + mv[0], cc + mv[1]
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and wars[nr][nc] == cur_color:
                    visited[nr][nc] = True
                    cur_pow += 1
                    q.append([nr, nc])     
    return cur_pow

cols, rows = map(int, input().split())
wars = []
for _ in range(rows):
    cur_row = list(str(input().rstrip()))
    wars.append(cur_row)
visited = [[False for _ in range(cols)] for _ in range(rows)]
ans_white = 0
ans_black = 0
for r in range(rows):
    for c in range(cols):
        if not visited[r][c]:
            cur_pow = bfs(r, c)
            if wars[r][c] == 'W':
                ans_white += (cur_pow ** 2)
            else:
                ans_black += (cur_pow ** 2)
print("%d %d" %(ans_white, ans_black))