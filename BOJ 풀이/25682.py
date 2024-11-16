# 체스판 칠하기 2
import sys
input = sys.stdin.readline

rows, cols, chess_size = map(int, input().split())
board = []
for _ in range(rows):
    cur_line = list(str(input().rstrip()))
    board.append(cur_line)
min_change = chess_size * chess_size
for cur_row in range(0, rows - (chess_size - 1)):
    for cur_col in range(0, cols - (chess_size -1)):
        white_start_count = 0
        black_start_count = 0
        for i in range(cur_row, cur_row+chess_size):
            for j in range(cur_col, cur_col+chess_size):
                if (i+j)%2 == 0 and board[i][j] == 'B':
                    white_start_count += 1
                elif (i+j)%2 == 1 and board[i][j] == 'W':
                    white_start_count += 1
        black_start_count = chess_size * chess_size - white_start_count
        min_change = min(min_change, white_start_count, black_start_count)
    # 답이 확정일 경우 스킵.
    if min_change == 0:
        break
print(min_change)