import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    std = int(input())
    next_list = [0] * (std + 1)
    for i in range(1, std + 1):
        cur_next = int(input())
        next_list[i] = cur_next
    visited = [False] * (std + 1)
    visited[1] = True
    step = 0
    cur_std = 1
    get_jugyeong = False
    while True:
        step += 1
        next_std = next_list[cur_std]
        if next_std == std:
            get_jugyeong = True
            break
        elif visited[next_std]:
            break
        visited[next_std] = True
        cur_std = next_std
    if get_jugyeong:
        print(step)
    else:
        print(0)