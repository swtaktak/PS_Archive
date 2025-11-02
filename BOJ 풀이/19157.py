import sys
from collections import deque
mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]
input = sys.stdin.readline

def bfs(r, c, x):
    q = deque()
    q.append([r, c])
    visited[r][c] = x
    
    while q:
        cr, cc = q.popleft()
        for mv in mv_list:
            nr, nc = cr + mv[0], cc + mv[1]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == -1:
                if table[nr][nc] % 2 == 0:
                    visited[nr][nc] = x
                    q.append([nr, nc])
                else:
                    visited[nr][nc] = 0

N, Q = map(int, input().split())

col_list = list(map(int, input().split()))
row_list = list(map(int, input().split()))

table = [[0 for _ in range(N)] for _ in range(N)]

for c in range(N):
    for r in range(N):
        table[c][r] = col_list[c] + row_list[r]

visited = [[-1 for _ in range(N)] for _ in range(N)]
cur_group = 1
for r in range(N):
    for c in range(N):
        if visited[r][c] == -1:
            bfs(r, c, cur_group)
            cur_group += 1

for _ in range(Q):
    ra, ca, rb, cb = map(int, input().split())
    if visited[ra-1][ca-1] == visited[rb-1][cb-1]:
        print('YES')
    else:
        print('NO')