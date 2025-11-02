import sys
from collections import deque
mv_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 0
    while q:
        cx, cy = q.popleft()
        for mv in mv_list:
            nx, ny = cx + mv[0], cy + mv[1]
            if 0 <= nx < rows and 0 <= ny < cols and visited[nx][ny] == -1:
                if room[nx][ny] == 1 or room[nx][ny] == 3:
                    visited[nx][ny] = visited[cx][cy] + 1
                    q.append([nx, ny])
                elif room[nx][ny] == 0:
                    visited[nx][ny] = visited[cx][cy]
                    # 0은 이어서 다시 방문해야 한다.! 방향에 주의한다.
                    q.appendleft([nx, ny])

rows, cols = map(int, input().split())
jx, jy, crx, cry = map(int, input().split())
room = []
for r in range(rows):
    cur_r = list(str(input().rstrip()))
    for c in range(cols):
        if cur_r[c] not in ['*', '#']:
            cur_r[c] = int(cur_r[c])
        elif cur_r[c] == '*':
            cur_r[c] = 2
        else:
            cur_r[c] = 3
    room.append(cur_r)
# 주난이는 2로, 범인은 3으로
# 방문행렬을 정답으료 표현한다.
visited = [[-1 for _ in range(cols)] for _ in range(rows)]
bfs(jx-1, jy-1)
print(visited[crx-1][cry-1])