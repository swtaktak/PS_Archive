# 17302
# IDEA > 어차피 2번을 해서 안되는 애는 3번으로 추가 가능하다.
# white 0, black 1
mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]
import sys
input = sys.stdin.readline
rows, cols = map(int, input().split())

board = []
for _ in range(rows):
    cur_row = []
    cur_c = str(input().rstrip())
    for c in cur_c:
        if c == 'W':
            cur_row.append(0)
        else:
            cur_row.append(1)
    board.append(cur_row)
    

ans = [[2 for _ in range(cols)] for _ in range(rows)]

for r in range(rows):
    for c in range(cols):
        for mv in mv_list:
            nr = r + mv[0]
            nc = c + mv[1]
            if 0 <= nr < rows and 0 <= nc < cols:
                board[nr][nc] = 1 - board[nr][nc]
                

# 여기서 2번을 해서 안된 애를 체크한다.
# 흑색인 애는 한번 더 눌렸어야 한다.

for r in range(rows):
    for c in range(cols):
        if board[r][c] == 1:
            ans[r][c] = 3

print(1)
for r in range(rows):
    print(''.join(str(x) for x in ans[r]))