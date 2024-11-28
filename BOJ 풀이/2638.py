
# idea / 오히려 공기를 판단한다.
# 치즈 칸을 모두 저장한 다음. 치즈 칸을 모두 또 bfs를 한다. 
# # 바깥 칸이 두개 이상일 경우에는 무조건 치즈를 제거하고, 해당 맵을 3으로 교체
# 그리고, 새 좌표를 air_list로 넣어서, 또 탐색 그리고 반복한다.
import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]

def cheese_control(cheese_queue, maps):
    # 치즈가 녹는지 확인. 녹지 않은 치즈 개수를 유지하기 위해 전역변수 고려.
    global left_cheese
    cur_try = left_cheese
    del_cheese = []
    for _ in range(cur_try):
        cx, cy = cheese_queue.popleft()
        cur_cnt = 0
        for mv in mv_list:
            nx, ny = cx + mv[0], cy + mv[1]
            if 0 <= nx < rows and 0 <= ny < cols:
                if maps[nx][ny] == 3:
                    cur_cnt += 1
        if cur_cnt >= 2:
            del_cheese.append([cx, cy])
            left_cheese -= 1
            air_queue.append([cx, cy]) # 녹은 치즈는 외부 공기가 된다.
        else:
            cheese_queue.append([cx, cy])
    # 녹을 치즈를 모두 한번에 확인한 다음에 지도에 반영해야 한다.
    for dx, dy in del_cheese:
        maps[dx][dy] = 3
    return maps


def air_bfs(visited, air_queue, maps):
    while air_queue:
        cx, cy = air_queue.popleft()
        for mv in mv_list:
            nx, ny = cx + mv[0], cy + mv[1]
            if 0 <= nx < rows and 0 <= ny < cols:
                # 현재 외부인데, 외부로 적용되지 않은 공기는 0번이다.
                if not visited[nx][ny] and maps[nx][ny] == 0:
                    maps[nx][ny] = 3
                    visited[nx][ny] = True
                    air_queue.append([nx, ny])
    return maps

rows, cols = map(int, input().split())
maps = []
air_queue = deque()
cheese_queue = deque()

for i in range(rows):
    cur_row = list(map(int, input().split()))
    for j in range(cols):
        if cur_row[j] == 1:
            cheese_queue.append([i, j])
        elif [i, j] in ([0, 0], [0, cols-1], [rows-1, 0], [rows-1, cols-1]):
            cur_row[j] = 3 # 바깥 공기는 3이다.
            air_queue.append([i, j])
    maps.append(cur_row)
    
left_cheese = len(cheese_queue)
visited = [[False for _ in range(cols)] for _ in range(rows)]
for [i, j] in ([0, 0], [0, cols-1], [rows-1, 0], [rows-1, cols-1]):
    visited[i][j] = True

day = 0
while left_cheese > 0:
    maps = air_bfs(visited, air_queue, maps)
    maps = cheese_control(cheese_queue, maps)
    day += 1
    
print(day)