import sys
from collections import deque
mv_list = [[2, 1], [2, -1], [-2, 1], [-2, -1],
           [1, 2], [1, -2], [-1, 2], [-1, -2]]
input = sys.stdin.readline

def bfs(sx, sy, ex, ey):
    q = deque()
    q.append([sx, sy])
    visited[sx][sy] = 0
    
    while q:
        cx, cy = q.popleft()
        if cx == ex and cy == ey:
            break
        for mv in mv_list:
            nx, ny = cx + mv[0], cy + mv[1]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == -1:
                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append([nx, ny])

T = int(input())
for _ in range(T):
    N = int(input())
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    bfs(sx, sy, ex, ey)
    print(visited[ex][ey])