import sys
from collections import deque
input = sys.stdin.readline
mv_list = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

def bfs(sr, sc, fr, fc):
    q = deque()
    q.append((sr, sc))
    
    while q:
        cr, cc = q.popleft()
        if cr == fr and cc == fc:
            break
        for mv in mv_list:
            nr = cr + mv[0]
            nc = cc + mv[1]
            
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == 40001:
                    visited[nr][nc] = visited[cr][cc] + 1
                    q.append((nr, nc))
                    
    if visited[fr][fc] == 40001:
        return -1
    else:
        return visited[fr][fc]

N = int(input())
sr, sc, fr, fc = map(int, input().split())
visited = [[40001 for _ in range(N)] for _ in range(N)]
visited[sr][sc] = 0

answer = bfs(sr, sc, fr, fc)
print(answer)