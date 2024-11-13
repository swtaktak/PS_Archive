import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, friend_list, visited):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    
    while queue:
        cur_v = queue.popleft()
        nv_list = friend_list[cur_v]
        for nv in nv_list:
            if visited[nv] == -1:
                visited[nv] = visited[cur_v] + 1
                queue.append(nv)
    return sum(visited[1:])

user, rel = map(int, input().split())
kevin_list = [0] * (user + 1)
friend_list = [[] for _ in range(user+1)]

for _ in range(rel):
    a, b = map(int, input().split())
    friend_list[a].append(b)
    friend_list[b].append(a)

for i in range(1, user+1):
    visited = [-1] * (user + 1)
    kevin_val = bfs(i, friend_list, visited)
    kevin_list[i] = kevin_val
kevin_list[0] = 999999999
min_val = min(kevin_list)
print(kevin_list.index(min_val))