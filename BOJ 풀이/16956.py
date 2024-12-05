import sys
input = sys.stdin.readline
mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]
rows, cols = map(int, input().split())

def print_field(field):
    for i in range(rows):
        print(''.join(field[i]))

def check_field(field):
    for i in range(rows):
        cur_row = field[i]
        for j in range(1, cols):
            if (cur_row[j] == 'W' and cur_row[j-1] == 'S') or (cur_row[j] == 'S' and cur_row[j-1] == 'W'):
                return False
    for i in range(cols):
        cur_col = [x[i] for x in field]
        for j in range(1, rows):
            if (cur_col[j] == 'W' and cur_col[j-1] == 'S') or (cur_col[j] == 'S' and cur_col[j-1] == 'W'):
                return False
    return True    

def make_fence(field):
    for i in range(rows):
        for j in range(cols):
            if field[i][j] == 'W':
                for mv in mv_list:
                    nx, ny = i + mv[0], j + mv[1]
                    if 0 <= nx < rows and 0 <= ny < cols:
                        if field[nx][ny] == '.':
                            field[nx][ny] = 'D'

field = []
sheep_cnt = 0
wolf_cnt = 0
for _ in range(rows):
    cur_row = list(str(input().rstrip()))
    for c in cur_row:
        if c == 'S':
            sheep_cnt += 1
        elif c == 'W':
            wolf_cnt += 1
    field.append(cur_row)

if sheep_cnt == 0 or wolf_cnt == 0:
    print(1)
    print_field(field)
elif not check_field(field):
    print(0)
else:
    print(1)
    make_fence(field)
    print_field(field)