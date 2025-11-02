import sys
input = sys.stdin.readline

def is_possible(x, y, nx, ny):
    for i in range(x, nx + 1):
        for j in range(y, ny + 1):
            if board[i][j] == 0:
                return False
    return True

def attach(x, y, nx, ny, num):
    for i in range(x, nx + 1):
        for j in range(y, ny + 1):
            board[i][j] = num
            
def dfs(level, cur_one_size):
    global answer
    if cur_one_size == 0:
        answer = min(answer, level)
        return
    for i in range(0, 10):
        for j in range(0, 10):
            if board[i][j] == 1:
                for p in range(5):
                    ni = i + p
                    nj = j + p
                    if paper_size[p] > 0 and ni < 10 and nj < 10:
                        if is_possible(i, j, ni, nj):
                            attach(i, j, ni, nj, 0)
                            paper_size[p] -= 1
                            dfs(level + 1, cur_one_size - p ** 2)
                            attach(i, j, ni, nj, 1)
                            paper_size[p] += 1
            return
board = []
paper_size = [5, 5, 5, 5, 5]
answer = 26
one_size = 0
for _ in range(10):
    cur_row = list(map(int, input().split()))
    board.append(cur_row)
    for c in cur_row:
        if c == 1:
            one_size += 1
dfs(0, one_size)

if answer == 26:
    print(-1)
else:
    print(answer)