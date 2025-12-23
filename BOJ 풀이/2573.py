# 2573 빙산
import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def bfs(r, c, visited):
    q = deque()
    visited[r][c] = True
    q.append((r, c))
    
    while q:
        cr, cc = q.popleft()
        for mv in mv_list:
            nr = cr + mv[0]
            nc = cc + mv[1]
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                if maps[nr][nc] > 0:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    return

def two_piece_check(maps):
    piece = 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if not visited[r][c] and maps[r][c] != 0:
                bfs(r, c, visited)
                piece += 1
    if piece >= 2:
        return True
    else:
        return False

rows, cols = map(int, input().split())
maps = []
for _ in range(rows):
    maps.append(list(map(int, input().split())))
    

step = 0
two_piece_flag = False

while True:
    all_melt_flag = True
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] != 0:
                all_melt_flag = False
                break
        if not all_melt_flag:
            break
    
    if all_melt_flag:
        break
    
    if two_piece_check(maps):
        two_piece_flag = True
        break
        
    # 두 조각이 아니므로, 빙산을 녹인다.
    new_map = [[0 for _ in range(cols)] for _ in range(rows)]
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if maps[r][c] != 0:
                water_cnt = 0
                for mv in mv_list:
                    nr = r + mv[0]
                    nc = c + mv[1]
                    if maps[nr][nc] == 0:
                        water_cnt += 1
                new_map[r][c] = max(0, maps[r][c] - water_cnt)
    step += 1
    maps = new_map

if two_piece_flag:
    print(step)
else:
    print(0)