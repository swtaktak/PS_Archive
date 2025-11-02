import sys
from collections import deque
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def bfs(r, c):
    q = deque()
    q.append([r, c])
    visited[r][c] = True
    
    while q:
        cr, cc = q.popleft()
        for mv in mv_list:
            nr, nc = cr + mv[0], cc + mv[1]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and space[nr][nc] == "*":
                    visited[nr][nc] = True
                    q.append([nr, nc])
            
input = sys.stdin.readline
N = int(input())
space = []
for _ in range(N):
    cur_row = list(str(input().rstrip()))
    space.append(cur_row)
    
cur_cnt = 0
visited = [[False for _ in range(N)] for _ in range(N)]

for r in range(N):
    for c in range(N):
        if not visited[r][c] and space[r][c] == '*':
            cur_cnt += 1
            bfs(r, c)

print(cur_cnt)