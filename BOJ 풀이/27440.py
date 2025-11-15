import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    q = deque()
    visited[start] = True
    q.append((start, 0))
    
    while q:
        cur_num, cur_try = q.popleft()
        if cur_num == 1:
            return cur_try
        if cur_num - 1 not in visited:
            visited[cur_num - 1] = True
            q.append((cur_num - 1, cur_try + 1))
        if cur_num % 2 == 0 and cur_num // 2 not in visited:
            visited[cur_num // 2] = True
            q.append((cur_num // 2, cur_try + 1))
        if cur_num % 3 == 0 and cur_num // 3 not in visited:
            visited[cur_num // 3] = True
            q.append((cur_num // 3, cur_try + 1))
            
target = int(input())
visited = {}
ans = bfs(target)
print(ans)