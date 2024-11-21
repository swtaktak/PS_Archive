import sys
import copy
input = sys.stdin.readline
move_keyword = ['L', 'R', 'U', 'D']
# 0을 우측으로 옮기는 상황
def zero_move(a):
    length = len(a)
    result = []
    for cur_a in a:
        if cur_a != 0:
            result.append(cur_a)
    while len(result) < length:
        result.append(0)
    return result
    
def move_left(board):
    for i in range(N):
        # step 1 / 0을 몰아준다.
        cur_row = board[i]
        cur_row = zero_move(cur_row)
        # step 2 / 좌우가 같으면 좌측에 2배, 우측에 0을 준다.
        for j in range(1, N):
            if cur_row[j-1] == cur_row[j]:
                cur_row[j-1] *= 2
                cur_row[j] = 0
        cur_row = zero_move(cur_row)
        for j in range(N):
            board[i][j] = cur_row[j]
    return board

def move_right(board):
    for i in range(N):
        cur_row = board[i][::-1]
        # step 1 / 뒤집어서 0을 몰아주면 된다.
        cur_row = zero_move(cur_row)
        # step 2 / 좌우가 같으면 좌측에 2배, 우측에 0을 준다.
        for j in range(1, N):
            if cur_row[j-1] == cur_row[j]:
                cur_row[j-1] *= 2
                cur_row[j] = 0
        cur_row = zero_move(cur_row)[::-1]
        for j in range(N):
            board[i][j] = cur_row[j]
    return board

def move_up(board):
    for i in range(N):
        cur_row = []
        for j in range(N):
            cur_row.append(board[j][i])
        cur_row = zero_move(cur_row)
        # step 2 / 좌우가 같으면 좌측에 2배, 우측에 0을 준다.
        for j in range(1, N):
            if cur_row[j-1] == cur_row[j]:
                cur_row[j-1] *= 2
                cur_row[j] = 0
        cur_row = zero_move(cur_row)
        for j in range(N):
            board[j][i] = cur_row[j]
    return board
        
def move_down(board):
    for i in range(N):
        cur_row = []
        for j in range(N):
            cur_row.append(board[j][i])
        cur_row = cur_row[::-1]
        cur_row = zero_move(cur_row)
        # step 2 / 좌우가 같으면 좌측에 2배, 우측에 0을 준다.
        for j in range(1, N):
            if cur_row[j-1] == cur_row[j]:
                cur_row[j-1] *= 2
                cur_row[j] = 0
        cur_row = zero_move(cur_row)[::-1]
        for j in range(N):
            board[j][i] = cur_row[j]
    return board

def dfs(level, key_list):
    global answer
    if level == 10:
        cur_try = copy.deepcopy(board)
        for k in key_list:
            if k == 'L':
                cur_try = move_left(cur_try)
            elif k == 'R':
                cur_try = move_right(cur_try)
            elif k == 'U':
                cur_try = move_up(cur_try)
            elif k == 'D':
                cur_try = move_down(cur_try)
        max_val = 0
        for i in range(N):
            for j in range(N):
                max_val = max(max_val, cur_try[i][j])
        answer = max(max_val, answer)
        return
    else:
        for m in move_keyword:
            key_list.append(m)
            dfs(level + 1, key_list)
            key_list.pop()

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
answer = 0
dfs(0, [])
print(answer)