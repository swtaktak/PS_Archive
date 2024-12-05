import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def barrier_bfs(i, j, open_cnt, connect_list):
    q = deque()
    q.append([i, j])
    open_check[i][j] = open_cnt
    cur_ctry_cnt = 1
    cur_pop_cnt = land[i][j]
    
    while q:
        cx, cy = q.popleft()
        for mv in mv_list:
            nx, ny = cx + mv[0], cy + mv[1]
            if 0 <= nx < N and 0 <= ny < N:
                if open_check[nx][ny] == -1 and min_cut <= abs(land[cx][cy] - land[nx][ny]) <= max_cut:
                    open_check[nx][ny] = open_cnt
                    cur_ctry_cnt += 1
                    cur_pop_cnt += land[nx][ny]
                    q.append([nx, ny])
    connect_list[open_cnt] = cur_pop_cnt // cur_ctry_cnt
    
def barrier_open(land):
    open_cnt = 0
    connect_list = {}
    for i in range(N):
        for j in range(N):
            if open_check[i][j] == -1:
                barrier_bfs(i, j, open_cnt, connect_list)
                open_cnt += 1
    return connect_list

N, min_cut, max_cut = map(int, input().split())
land = []
for _ in range(N):
    land.append(list(map(int, input().split())))
    
day = 0
while True:
    open_check = [[-1 for _ in range(N)] for _ in range(N)]
    # 인구 이동의 정보를 받아온다.
    connect_list = barrier_open(land)
    if len(connect_list) == N ** 2:
        break
    else:
        for i in range(N):
            for j in range(N):
                if open_check[i][j] in connect_list:
                    land[i][j] = connect_list[open_check[i][j]]
        day += 1

print(day)