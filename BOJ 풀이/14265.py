import sys
from collections import deque
input = sys.stdin.readline

visited = set()
start, lb, rb = map(int, input().split())

q = deque()

q.append(start)
answer = 0
while q:
    cur_num = q.popleft()
    if lb <= cur_num <= rb:
        answer += 1
    if cur_num in visited or cur_num > rb:
        continue
    visited.add(cur_num)
    
    if cur_num % 2 == 1 and cur_num * 2 <= rb and cur_num * 2 not in visited:
        q.append(cur_num * 2)
    else:
        if cur_num + 1 <= rb and cur_num + 1 not in visited:
            q.append(cur_num + 1)
        if cur_num * 2 <= rb and cur_num * 2 not in visited:
            q.append(cur_num * 2)
print(answer)
    