# 32207
import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]
rows, cols, pick_max = map(int, input().split())
ruby_list = []
for i in range(rows):
    cur_row = list(map(int, input().split()))
    for j in range(cols):
        ruby_list.append([cur_row[j], i, j])
ruby_list.sort(key = lambda x: x[0], reverse = True)

pick_list = []
for cur_r in ruby_list:
    if not pick_list:
        pick_list.append(cur_r)
    else:
        cx, cy = cur_r[1], cur_r[2]
        not_nb_flag = True
        for mv in mv_list:
            nx, ny = cx + mv[0], cy + mv[1]
            for p in pick_list:
                if p[1] == nx and p[2] == ny:
                    not_nb_flag = False
                    break
            if not not_nb_flag:
                True
        if not_nb_flag:
            pick_list.append(cur_r)
    if len(pick_list) == pick_max:
        break
ans = 0
for p in pick_list:
    ans += p[0]
print(ans)