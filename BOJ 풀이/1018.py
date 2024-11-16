import sys
input = sys.stdin.readline

rows, cols = map(int, input().split())
board = []
for _ in range(rows):
    cur_line = list(str(input().rstrip()))
    board.append(cur_line)
min_change = 64
for cur_row in range(0, rows - 7):
    for cur_col in range(0, cols - 7):
        white_start_count = 0
        black_start_count = 0
        for i in range(cur_row, cur_row+8):
            for j in range(cur_col, cur_col+8):
                if (i+j)%2 == 0 and board[i][j] == 'B':
                    white_start_count += 1
                elif (i+j)%2 == 1 and board[i][j] == 'W':
                    white_start_count += 1
                # 상호 대칭이다. 64개에서 빼면 된다.
                black_start_count = 64 - white_start_count
        min_change = min(min_change, white_start_count, black_start_count)
print(min_change)