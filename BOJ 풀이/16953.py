from collections import deque
queue = deque()
a, b = map(int, input().split())

answer = -1
count_list = []
queue.append((a, 0))
while queue:
    cur_num, cur_cnt = queue.popleft()
    if cur_num == b:
        answer = cur_cnt
        break
    else:
        for i in (cur_num * 2, 10*cur_num + 1):
            if i <= b:
                queue.append((i, cur_cnt +1))
if answer == -1:
    print(answer)
else:
    print(answer + 1)