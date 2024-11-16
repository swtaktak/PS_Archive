import sys
from collections import deque
input = sys.stdin.readline

subin, brother = map(int, input().split())
visited = [1e9] * 100001
visited[subin] = 0

queue = deque()
min_time = 100001
cur_case = 0
queue.append((subin, 0))
while queue:
    cur_pos, cur_time = queue.popleft()
    if cur_pos == brother:
        if cur_time < min_time:
            cur_case = 1
            min_time = cur_time
        elif cur_time == min_time:
            cur_case += 1
    else:
        for new_pos in [cur_pos + 1, cur_pos -1, cur_pos * 2]:
            if 0 <= new_pos <= 100000:
                if visited[new_pos] >= cur_time:
                    visited[new_pos] = cur_time
                    queue.append((new_pos, cur_time + 1))
print(min_time)
print(cur_case)