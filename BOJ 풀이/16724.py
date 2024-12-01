import sys
from collections import deque
input = sys.stdin.readline
mv_dict = {'U': [-1, 0], 'R': [0, 1], 'L': [0, -1], 'D': [1, 0]}

def get_top_parent(x):
    if x != parent_list[x]:
        parent_list[x] = get_top_parent(parent_list[x])
    return parent_list[x]

def union(x, y):
    x = get_top_parent(x)
    y = get_top_parent(y)
    if x > y:
        parent_list[x] = y
    else:
        parent_list[y] = x

def follow_path(sx, sy, cur_gp):
    global parent_list
    visited[sx][sy] = cur_gp
    parent_list.append(cur_gp)
    while True:
        cur_order = mv_dict[maps[sx][sy]]
        nx, ny = sx+cur_order[0], sy+cur_order[1]
        if visited[nx][ny] == -1:
            visited[nx][ny] = cur_gp
            sx, sy = nx, ny
        elif visited[nx][ny] == cur_gp:
            break
        elif visited[nx][ny] < cur_gp:
            union(cur_gp, visited[nx][ny])
            break

rows, cols = map(int, input().split())
maps = []
for _ in range(rows):
    cur_row = list(str(input().rstrip()))
    maps.append(cur_row)

visited = [[-1 for _ in range(cols)] for _ in range(rows)]
# 또 유니온 파인드에서 막힌다 ㅠㅠㅠ
# 연결 상태를 만들어, 개수를 세면 된다.
parent_list = []
graph = []

cur_group = 0
for i in range(rows):
    for j in range(cols):
        if visited[i][j] == -1:
            follow_path(i, j, cur_group)
            cur_group += 1
print(len(list(set(parent_list))))