import sys
input = sys.stdin.readline
tetra_map = []
rows, cols = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(rows):
    cur_row = list(map(int, input().split()))
    tetra_map.append(cur_row)

max_sum = 0
def tetra_max(cur_x, cur_y, prev_x, prev_y, level, cur_sum):
    global max_sum
    if level == 4:
        if max_sum < cur_sum:
            max_sum = cur_sum
        return
    else:
        for k in range(4):
            new_x = cur_x + dx[k]
            new_y = cur_y + dy[k]
            if 0 <= new_x < rows and 0 <= new_y < cols:
                if new_x != prev_x or new_y != prev_y:
                    tetra_max(new_x, new_y, cur_x, cur_y, level + 1,
                              cur_sum + tetra_map[new_x][new_y])
# DFS로는 ㅗ 모양 불가./회전 고려하기.
def t_sum(i, j):
    global max_sum
    # ㅗ 방향 체크
    if i-1 >= 0 and j+2 <= cols-1:
        cur_sum = tetra_map[i][j] + tetra_map[i][j+1] + tetra_map[i-1][j+1] + tetra_map[i][j+2]
        if cur_sum >= max_sum:
            max_sum = cur_sum
    # ㅜ 방향 체크        
    if i+1 <= rows-1 and j+2 <= cols-1:
        cur_sum = tetra_map[i][j] + tetra_map[i][j+1] + tetra_map[i+1][j+1] + tetra_map[i][j+2]
        if cur_sum >= max_sum:
            max_sum = cur_sum
    # ㅏ 방향 체크        
    if i+2 <= rows-1 and j+1 <= cols-1:
        cur_sum = tetra_map[i][j] + tetra_map[i+1][j] + tetra_map[i+1][j+1] + tetra_map[i+2][j]
        if cur_sum >= max_sum:
            max_sum = cur_sum
    # ㅓ 방향 체크        
    if i+2 <= rows-1 and j-1 >= 0:
        cur_sum = tetra_map[i][j] + tetra_map[i+1][j] + tetra_map[i+1][j-1] + tetra_map[i+2][j]
        if cur_sum >= max_sum:
            max_sum = cur_sum

for i in range(rows):
    for j in range(cols):
        tetra_max(i, j, -1, -1, 1, tetra_map[i][j])
        t_sum(i, j)

print(max_sum)