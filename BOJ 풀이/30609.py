# 30609 Alloys
import sys
input = sys.stdin.readline

N = int(input())

val_dict = {}

for _ in range(N):
    cur_list = list(map(str, input().rstrip().split()))
    cur_data = float(cur_list[1]), float(cur_list[2])
    cur_name = cur_list[0]
    
    val_dict[cur_name] = cur_data
    
val_dict = sorted(
    val_dict.items(),
    key = lambda x: (-x[1][0], -x[1][1])
)

max_cond = -1e9
ans_list = []
min_flex = 1e9
for name, (flex, cond) in val_dict:
    if cond >= max_cond:
        ans_list.append(name)
        max_cond = cond

ans_list.sort()

for a in ans_list:
    print(a, end = " ")