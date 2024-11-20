import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
rows, cols = map(int, input().split())
visited = [[False for _ in range(cols)] for _ in range(rows)]
maps = []
answer_maps = [[0 for _ in range(cols)] for _ in range(rows)]
connected_dict = {}

for _ in range(rows):
    cur_row = list(str(input().rstrip()))
    cur_row = [int(x) for x in cur_row]
    cur_row = [-1 if x == 1 else x for x in cur_row]
    # 1칸짜리 빈 공간이 있어 벽과 구분이 불가능해서 벽을 -1로 치환할 거임    
    maps.append(cur_row)


def bfs(x, y, cur_area_num):
    global connected_dict
    count = 1
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    maps[x][y] = cur_area_num
    
    while queue:
        cx, cy = queue.popleft()
        for mv in mv_list:
            nx, ny = cx + mv[0], cy + mv[1]
            if 0 <= nx < rows and 0 <= ny < cols:
                if not visited[nx][ny] and maps[nx][ny] == 0:
                    visited[nx][ny] = True
                    count += 1
                    maps[nx][ny] = cur_area_num
                    queue.append([nx, ny])
                    
    connected_dict[cur_area_num] = count
    return maps                

cur_area_num = 1
for i in range(rows):
    for j in range(cols):
        # 빈 공간일 경우
        if maps[i][j] == 0 and not visited[i][j]:
            maps = bfs(i, j, cur_area_num)
            cur_area_num += 1

# 마지막으로 판단
for i in range(rows):
    for j in range(cols):
        if maps[i][j] != -1:
            answer_maps[i][j] == 0
        else:
            connect_list = []
            if i-1 >= 0:
                if maps[i-1][j] != -1:
                    connect_list.append(maps[i-1][j])
            if i+1 < rows:
                if maps[i+1][j] != -1:
                    connect_list.append(maps[i+1][j])
            if j-1 >= 0:
                if maps[i][j-1] != -1:
                    connect_list.append(maps[i][j-1])
            if j+1 < cols:
                if maps[i][j+1] != -1:
                    connect_list.append(maps[i][j+1])
            connect_list = list(set(connect_list))
            
            if len(connect_list) == 0:
                answer_maps[i][j] = 1
            else:
                cur_sum = 1
                for c in connect_list:
                    cur_sum += connected_dict[c]
                answer_maps[i][j] = cur_sum % 10
        print(answer_maps[i][j], end = "")
    print()
