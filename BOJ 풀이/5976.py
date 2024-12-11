# 달팽이 집을 집시다
import sys
input = sys.stdin.readline
N = int(input())
mv_list = [[0, 1], [1, 0], [0, -1], [-1, 0]]
mv_type = 0

ans = [[0 for _ in range(N)] for _ in range(N)]

cur_x = 0
cur_y = 0
for i in range(1, N**2 + 1):
    ans[cur_x][cur_y] = i
    if i == N ** 2:
        break
    else:
        while True:
            mv = mv_list[mv_type]
            nx, ny = cur_x + mv[0], cur_y + mv[1]
            if 0 <= nx < N and 0 <= ny < N and ans[nx][ny] == 0:
                cur_x = nx
                cur_y = ny
                break
            else:
                mv_type = (mv_type + 1) % 4
for r in range(N):
    for c in range(N):
        print(ans[r][c], end = " ")
    print()