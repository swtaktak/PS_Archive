import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

def bfs(r, c):
    q = deque()
    visited[r][c] = True
    q.append([r, c])
    flag = True
    
    while q:
        cr, cc = q.popleft()
        for mv in mv_list:
            nr, nc = cr + mv[0], cc + mv[1]
            if 0 <= nr < rows and 0 <= nc < cols:
                if maps[nr][nc] > maps[r][c]:
                    flag = False
                if not visited[nr][nc] and maps[nr][nc] == maps[cr][cc]:
                    visited[nr][nc] = True
                    q.append([nr, nc])
    return flag

rows, cols = map(int, input().split())
maps = []
min_val = 10001
# 두 가지 이상의 값이 존재하는지 확인
two_type_flag = False

for _ in range(rows):
    cur_row = list(map(int, input().split()))
    for c in cur_row:
        if min_val > c:
            if min_val != 10001:
                two_type_flag = True
            min_val = c
        if min_val != c:
            two_type_flag = True
    maps.append(cur_row)

# 두 가지 이상의 값이 없으면 바로 1출력
if not two_type_flag:
    print(1)
else:
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    cnt = 0
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] > min_val and not visited[r][c]:
                cnt += bfs(r, c)
    print(cnt)