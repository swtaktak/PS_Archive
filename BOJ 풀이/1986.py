import sys
input = sys.stdin.readline
knight_mv_list = [[-2, -1], [-2, 1],
                  [-1, -2], [1, -2],
                  [2, -1], [2, 1],
                  [-1, 2], [1, 2]] 
rows, cols = map(int, input().split())
chess_board = [["O" for _ in range(cols)] for _ in range(rows)]
safe_space = rows*cols

# 기물 세팅 단계 _ 퀸
queen_list = list(map(int, input().split()))
queen_put_cnt = 0
cur_point = 1
queen_pos_list = []
while queen_put_cnt < queen_list[0]:
    qx, qy = queen_list[cur_point], queen_list[cur_point + 1]
    cur_point += 2
    queen_put_cnt += 1
    queen_pos_list.append((qx-1, qy-1))
    chess_board[qx-1][qy-1] = "Q"
    safe_space -= 1
    
# 기물 세팅 단계 _ 나이트
knight_list = list(map(int, input().split()))
knight_put_cnt = 0
cur_point = 1
knight_pos_list = []
while knight_put_cnt < knight_list[0]:
    qx, qy = knight_list[cur_point], knight_list[cur_point + 1]
    cur_point += 2
    knight_put_cnt += 1
    knight_pos_list.append((qx-1, qy-1))
    chess_board[qx-1][qy-1] = "K"
    safe_space -= 1
    
# 기물 세팅 단계 _ 폰
pawn_list = list(map(int, input().split()))
pawn_put_cnt = 0
cur_point = 1
while pawn_put_cnt < pawn_list[0]:
    qx, qy = pawn_list[cur_point], pawn_list[cur_point + 1]
    cur_point += 2
    pawn_put_cnt += 1
    chess_board[qx-1][qy-1] = "P"
    safe_space -= 1
    
block_list = ['K', 'P', 'Q']
# 나이트의 경우 들어갈 수 있으면 끝난다.
for cur_knight in knight_pos_list:
    cur_x, cur_y = cur_knight[0], cur_knight[1]
    for kn in knight_mv_list:
        nx = cur_x+kn[0]
        ny = cur_y+kn[1]
        if 0 <= nx < rows and 0 <= ny < cols:
            if chess_board[nx][ny] not in block_list:
                if chess_board[nx][ny] == "O":
                    chess_board[nx][ny] = "X"
                    safe_space -= 1

# 퀸의 경우 막히면 끝난다. 이미 나이트가 공격한 칸은 겹쳐 세지 않음에 주의한다.
for cur_queen in queen_pos_list:
    cur_x, cur_y = cur_queen[0], cur_queen[1]
    # row 방향 감소
    for i in range(cur_x, -1, -1):
        if i == cur_x : pass
        elif chess_board[i][cur_y] == "O":
            chess_board[i][cur_y] = "X"
            safe_space -= 1
        elif chess_board[i][cur_y] in block_list:
            # 막혀서 더 이상 공격이 안됨
            break
    # row 방향 증가.
    for i in range(cur_x, rows):
        if i == cur_x: pass
        elif chess_board[i][cur_y] == "O":
            chess_board[i][cur_y] = "X"
            safe_space -= 1
        elif chess_board[i][cur_y] in block_list:
            # 막혀서 더 이상 공격이 안됨
            break
    # col 방향 감소
    for i in range(cur_y, -1, -1):
        if i == cur_y : pass
        elif chess_board[cur_x][i] == "O":
            chess_board[cur_x][i] = "X"
            safe_space -= 1
        elif chess_board[cur_x][i] in block_list:
            # 막혀서 더 이상 공격이 안됨
            break
    # col 방향 증가
    for i in range(cur_y, cols):
        if i == cur_y : pass
        elif chess_board[cur_x][i] == "O":
            chess_board[cur_x][i] = "X"
            safe_space -= 1
        elif chess_board[cur_x][i] in block_list:
            # 막혀서 더 이상 공격이 안됨
            break
    # 북서쪽 방향 : 감소 감소
    nx, ny = cur_x, cur_y
    while True:
        nx -= 1
        ny -= 1
        if 0 <= nx < rows and 0 <= ny < cols:
            if chess_board[nx][ny] in block_list:
                break
            elif chess_board[nx][ny] == "O":
                chess_board[nx][ny] = "X"
                safe_space -= 1
        else:
            break
    # 북동쪽 방향 : 감소 증가
    nx, ny = cur_x, cur_y
    while True:
        nx -= 1
        ny += 1
        if 0 <= nx < rows and 0 <= ny < cols:
            if chess_board[nx][ny] in block_list:
                break
            elif chess_board[nx][ny] == "O":
                chess_board[nx][ny] = "X"
                safe_space -= 1
        else:
            break
    # 남동쪽 방향 : 증가 증가
    nx, ny = cur_x, cur_y
    while True:
        nx += 1
        ny += 1
        if 0 <= nx < rows and 0 <= ny < cols:
            if chess_board[nx][ny] in block_list:
                break
            elif chess_board[nx][ny] == "O":
                chess_board[nx][ny] = "X"
                safe_space -= 1
        else:
            break
    # 남서쪽 방향 : 증가 감소
    nx, ny = cur_x, cur_y
    while True:
        nx += 1
        ny -= 1
        if 0 <= nx < rows and 0 <= ny < cols:
            if chess_board[nx][ny] in block_list:
                break
            elif chess_board[nx][ny] == "O":
                chess_board[nx][ny] = "X"
                safe_space -= 1
        else:
            break
print(chess_board)
print(safe_space)