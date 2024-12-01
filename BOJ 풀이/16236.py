import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[-1, 0], [0, -1], [0, 1], [1, 0]]
INF = 1e9
# 우선순위를 bfs만으로는 무리여서 싹 다 갈아야 한다.
# 여기엔 거리 행렬을 담는다.
def bfs(sx, sy):
    global shark_size
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0
    
    while q:
        sx, sy = q.popleft()
        for mv in mv_list:
            nx, ny = sx+mv[0], sy+mv[1]
            if 0 <= nx < N and 0 <= ny < N:
                if sea[nx][ny] <= shark_size and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[sx][sy] + 1
                    q.append((nx, ny))
    return dist

def eat_fish(dist):
    global shark_size
    min_dist = INF
    for i in range(N):
        for j in range(N):
            # 먹을 수 있다면
            if sea[i][j] < shark_size and sea[i][j] >= 1 and dist[i][j] > 0:
                if dist[i][j] < min_dist:
                    # 정답 좌표는 책 읽는 순서로
                    rx, ry = i, j
                    min_dist = dist[i][j]
    if min_dist == INF:
        return [False, INF, -1, -1]
    else:
        return [True, min_dist, rx, ry]
    
N = int(input())
fish_count = 0
sea = []
shark_size = 2
shark_eat_cnt = 0
fish_time = 0
# 맵 입력과 초기 위치 찾기
for i in range(N):
    cur_row = list(map(int, input().split()))
    for j in range(N):
        if cur_row[j] == 9:
            sx, sy = i, j
            cur_row[j] = 0
        elif cur_row[j] > 0:
            fish_count += 1
    sea.append(cur_row)
while True:
    dist_matrix = bfs(sx, sy)
    result = eat_fish(dist_matrix)
    if result[0]:
        fish_time += result[1]
        sx = result[2]
        sy = result[3]
        sea[sx][sy] = 0
        shark_eat_cnt += 1
        if shark_eat_cnt == shark_size:
            shark_size += 1
            shark_eat_cnt = 0
    else:
        break
print(fish_time)