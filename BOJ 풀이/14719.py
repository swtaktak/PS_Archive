import sys
input = sys.stdin.readline
rows, cols = map(int, input().split())

world = [[0 for _ in range(cols)] for _ in range(rows)]

h_list = list(map(int, input().split()))
for c in range(cols):
    cur_h = h_list[c]
    for r in range(rows-1, rows-1-cur_h, -1):
        world[r][c] = 1
# 1의 위치를 담은 뒤, 1위 위치를 재 탐색 하여, 간격을 계산한다.
# 간격 - 1을 모두 합치면 된다.
cnt = 0
for r in range(rows):
    one_pos = []
    for c in range(cols):
        if world[r][c] == 1:
            one_pos.append(c)
    if len(one_pos) >= 2:
        for i in range(1, len(one_pos)):
            cnt += (one_pos[i] - one_pos[i-1] - 1)
print(cnt)