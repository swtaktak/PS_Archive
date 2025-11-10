import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]


def bfs(r, c):
    global answer
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    
    while q:
        cr, cc = q.popleft()
        for mv in mv_list:
            nr, nc = cr + mv[0], cc + mv[1]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and map[nr][nc] == '.':
                    visited[nr][nc] = True
                    answer += 1
                    q.append((nr, nc))


N = int(input())
map = []
for i in range(N):
    cur_row = [ch for ch in input().rstrip()]
    if 'F' in cur_row:
        fr = i
        fc = cur_row.index('F')
    map.append(cur_row)

visited = [[False for _ in range(N)] for _ in range(N)]
answer = 0
bfs(fr, fc)
print(answer)