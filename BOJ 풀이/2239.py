import sys
input = sys.stdin.readline

def sudoku_conflict(cur_x, cur_y, cur_num, sudoku):
    # row check
    for i in range(9):
        if sudoku[cur_x][i] == cur_num:
            return False
    # col check
    for i in range(9):
        if sudoku[i][cur_y] == cur_num:
            return False
    # box check
    box_x = (cur_x//3) * 3
    box_y = (cur_y//3) * 3
    for i in range(box_x, box_x+3):
        for j in range(box_y, box_y+3):
            if sudoku[i][j] == cur_num:
                return False
    return True


sudoku = []
zero_pos = []
for i in range(9):
    cur_row = list(str(input().rstrip()))
    for j in range(9):
        if cur_row[j] == '0':
            zero_pos.append([i, j])
    sudoku.append(cur_row)
zero_cnt = len(zero_pos)    

def print_sudoku(sudoku):
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], end = "")
        print()

def dfs(fill_cnt):
    if fill_cnt == zero_cnt:
        print_sudoku(sudoku)
        exit()
    else:
        # 현재 제로 위치
        cur_x, cur_y = zero_pos[fill_cnt]
        for i in range(1, 10):
            # 만일 현재 숫자가 문제가 없다면
            if sudoku_conflict(cur_x, cur_y, str(i), sudoku):
                sudoku[cur_x][cur_y] = str(i)
                dfs(fill_cnt + 1)
                sudoku[cur_x][cur_y] = '0'
            
dfs(0) # 채운 zero 개수

