import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
girl = []

def s_over(coord_pick):
    s_cnt = 0
    y_cnt = 0
    for c in coord_pick:
        if girl[c[0]][c[1]] == 'Y':
            y_cnt += 1
        else:
            s_cnt += 1
    if s_cnt >= 4:
        return True
    else:
        return False

def connect(coord_pick):
    # 지도를 만들어 고른 사람을 1로 한다.
    maps = [[0 for _ in range(5)] for _ in range(5)]
    visited = [[False for _ in range(5)] for _ in range(5)]
    for c in coord_pick:
        maps[c[0]][c[1]] = 1
    q = deque()
    q.append([coord_pick[0][0], coord_pick[0][1]])
    visited[coord_pick[0][0]][coord_pick[0][1]] = True
    count = 0
    
    while q:
        cx, cy = q.popleft()
        count += 1
        for mv in mv_list:
            nx, ny = cx + mv[0], cy + mv[1]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append([nx, ny])
    if count == 7:
        return True
    else:
        return False
    
for _ in range(5):
    cur_list = list(str(input().rstrip()))
    girl.append(cur_list)

# 우선 좌표를 넣고 25개중 7개를 골라야 한다.
coord_list = []
for i in range(5):
    for j in range(5):
        coord_list.append([i, j])

visited = [False] * 25
answer = 0
coord_pick = []
def dfs_coord(level, cur_pos):
    global answer
    if level == 7:
        if s_over(coord_pick):
            if connect(coord_pick):
                answer += 1
        return
    
    for i in range(cur_pos, 25):
        if not visited[i]:
            visited[i] = True
            coord_pick.append(coord_list[i])
            dfs_coord(level + 1, i)
            visited[i] = False
            coord_pick.pop()
dfs_coord(0, 0)
print(answer)