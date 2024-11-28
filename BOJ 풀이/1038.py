from collections import deque
N = int(input())

if N >= 1023:
    print(-1)
else:
    queue = deque()
    for i in range(0, 10):
        queue.append(str(i))
    answer_list = []
    while queue:
        cur_num = int(queue.pop())
        answer_list.append(cur_num)
        last_digit = cur_num % 10
        for i in range(0, last_digit):
            queue.append(cur_num * 10 + i)
    answer_list.sort()
    print(answer_list[N])
