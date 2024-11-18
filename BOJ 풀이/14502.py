import sys
from collections import deque
import copy
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]

rows, cols = map(int, input().split())
lab = []
safe_list = []
virus_list = []
for i in range(rows):
    cur_row = list(map(int, input().split()))
    lab.append(cur_row)
    
for i in range(rows):
    for j in range(cols):
        if lab[i][j] == 0:
            safe_list.append((i, j))
        elif lab[i][j] == 2:
            virus_list.append((i, j))
     
def virus_bfs(cur_lab, cur_wall_list):
    for x, y in cur_wall_list:
        cur_lab[x][y] = 1
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    for x, y in virus_list:
        queue.append((x, y))
        visited[x][y] = True
        
    while queue:
        cur_x, cur_y = queue.popleft()
        for mv in mv_list:
            nx, ny = cur_x + mv[0], cur_y + mv[1]

            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx][ny] and cur_lab[nx][ny] == 0:
                    cur_lab[nx][ny] = 2
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    cur_safe_cnt = 0
    for i in range(rows):
        for j in range(cols):
            if cur_lab[i][j] == 0:
                cur_safe_cnt += 1
    return cur_safe_cnt

def wall_dfs(wall_cnt, cur_pos):
    global safe_spot
    if wall_cnt == 3:
        cur_lab = copy.deepcopy(lab)
        cur_safe_spot = virus_bfs(cur_lab, cur_wall_list)
        if cur_safe_spot > safe_spot:
            best_board = copy.deepcopy(cur_lab)
            safe_spot = cur_safe_spot
        return

    for i in range(cur_pos, len(safe_list)):
        # 현재 벽을 세울 위치
        cur_wall_pos = safe_list[i]
        cur_wall_list.append(cur_wall_pos)
        wall_dfs(wall_cnt + 1, i + 1)
        cur_wall_list.pop()
        
safe_spot = -1
cur_wall_list = []
wall_dfs(0, 0)
print(safe_spot)