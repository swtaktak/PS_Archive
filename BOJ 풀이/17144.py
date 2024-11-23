import sys
input = sys.stdin.readline
mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]
def dust_move(maps):
    for i in range(rows):
        for j in range(cols):
            # 만일 먼지가 있다면
            if maps[i][j][0] > 0:
                # 성공했다면
                move_amt = maps[i][j][0] // 5
                if move_amt > 0:
                    move_cnt = 0
                    for mv in mv_list:
                        nx, ny = i + mv[0], j + mv[1]
                        if 0 <= nx < rows and 0 <= ny < cols:
                            if maps[nx][ny][0] != -1:
                                maps[nx][ny][1] += move_amt
                                move_cnt += 1
                    maps[i][j][1] -= move_amt * move_cnt
    for i in range(rows):
        for j in range(cols):
            maps[i][j][0] += maps[i][j][1]
            maps[i][j][1] = 0
    return maps     

def upper_acw(board):
    # 반대로 땡겨버리면 된다.
    for i in range(air_up - 1, 0, -1):
        board[i][0][0] = board[i-1][0][0]
    for i in range(0, cols-1):
        board[0][i][0] = board[0][i+1][0]
    for i in range(0, air_up):
        board[i][-1][0] = board[i+1][-1][0]
    for i in range(cols-1, 0, -1):
        board[air_up][i][0] = board[air_up][i-1][0]
    board[air_up][1] = [0, 0]
    return board

def lower_cw(board):
    # 반대로 땡겨버리면 된다.
    for i in range(air_down + 1, rows - 1):
        board[i][0][0] = board[i+1][0][0]
    for i in range(0, cols-1):
        board[-1][i][0] = board[-1][i+1][0]
    for i in range(rows -1, air_down, -1):
        board[i][-1][0] = board[i-1][-1][0]
    for i in range(cols-1, 0, -1):
        board[air_down][i][0] = board[air_down][i-1][0]
    board[air_down][1] = [0, 0]
    return board
         
rows, cols, repeat_time = map(int, input().split())
maps = []
air_list = []
for i in range(rows):
    cur_row = list(map(int, input().split()))
    input_row = []
    for c in cur_row:
        input_row.append([c, 0]) # 현재 먼지량, 변화 먼지량
        if c == -1:
            air_list.append(i)
    maps.append(input_row)

air_up = air_list[0]
air_down = air_list[1]
for _ in range(repeat_time):
    maps = dust_move(maps)
    maps = upper_acw(maps)
    maps = lower_cw(maps)
    
answer = 0
for i in range(rows):
    for j in range(cols):
        if maps[i][j][0] > 0:
            answer += maps[i][j][0]
print(answer)
