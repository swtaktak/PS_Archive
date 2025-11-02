# 기본단위 = 시간 + 대수

import sys
from collections import deque
input = sys.stdin.readline
truck, lens, max_w = map(int, input().split())
ans_list = []

t_list = list(map(int, input().split()))

sum_w = 0
cur_time = 0
q = deque()

for _ in range(lens):
    q.append(0)

while q or t_list:
    if t_list:
        cur_t = t_list[-1]
        final_w = q.popleft()
        sum_w -= final_w
        if sum_w + cur_t <= max_w:
            sum_w += cur_t
            q.append(cur_t)
            t_list.pop()
        else:
            q.append(0)
    else:
        q.popleft()
    cur_time += 1

print(cur_time) 
   