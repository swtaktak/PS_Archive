import sys
input = sys.stdin.readline

step_dict = {}
for cur_start in range(1, 5001):
    start = cur_start
    cur_step = 1
    while True:
        start += 1
        if start % cur_step == 0:
            if start == cur_step ** 2:
                same_cut = cur_step # 여기부터는 등차다.
                break
            cur_step += 1
    if cur_step not in step_dict:
        step_dict[cur_step] = 1
    else:
        step_dict[cur_step] += 1
print(step_dict)