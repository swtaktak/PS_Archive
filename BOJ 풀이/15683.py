import sys
import copy
input = sys.stdin.readline
# 칠하는 것은 # 이 아니라 int 통일을 위해 7번으로 진행한다.
# 보드를 돌리기가 어렵다. deepcopy를 써서 돌려줄 애를 기억해서 돌려야 한다!
def fill_camera(chosen_way, cx, cy, maps):
    for cur_way in chosen_way:
        mv = mv_list[cur_way]
        nx = cx
        ny = cy
        while True:
            nx += mv[0]
            ny += mv[1]
            if 0 <= nx < rows and 0 <= ny < cols:
                if maps[nx][ny] == 6:
                    break
                elif maps[nx][ny] == 0:
                    maps[nx][ny] = 7
            else:
                break
        
mv_list = [[-1, 0], [1, 0], [0, -1], [0, 1]] # 위 아래 왼쪽 오른쪽
camera = [[], # 0번 없음
          [[0], [1], [2], [3]], # 1번이 선택 가능한 4방향,
          [[0, 1], [2, 3]], # 2번이 선택 가능한 2방향,
          [[0, 2], [0, 3], [1, 2], [1, 3]], # 3번이 선택 가능한 4방향
          [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]], # 4번이 선택 가능한 4방향
          [[0, 1, 2, 3]]] # 5번이 선택 가능한 1방향

rows, cols = map(int, input().split())
cur_space = rows * cols

maps = []
camera_pos = [] # 이거의 깊이 만큼 dfs를 돌려줄 예정이다
for i in range(rows):
    cur_row = list(map(int, input().split()))
    maps.append(cur_row)
    for j in range(cols):
        if cur_row[j] in [1, 2, 3, 4, 5]:
            camera_pos.append([cur_row[j], i, j]) # 카메라 번호, 행, 열

def dfs(num_camera, maps):
    global min_space
    if num_camera == len(camera_pos):
        count = 0
        for i in range(rows):
            for j in range(cols):
                if maps[i][j] == 0:
                    count += 1
        if count < min_space:
            min_space = count
        return
        
    temp_map = copy.deepcopy(maps) 
    cur_tv, cur_x, cur_y = camera_pos[num_camera]
    for cur_mode in camera[cur_tv]:
        fill_camera(cur_mode, cur_x, cur_y, temp_map)
        dfs(num_camera + 1, temp_map)
        # 보드를 초기화해서 카메라 방향을 돌려야 하니까
        temp_map = copy.deepcopy(maps)

min_space = 1e18
dfs(0, maps)
print(min_space)