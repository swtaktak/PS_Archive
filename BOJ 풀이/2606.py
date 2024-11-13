import sys
from collections import deque
input = sys.stdin.readline
def bfs(visited, vertex_dict):
    queue = deque()
    visited[1] = True
    queue.append(1)
    
    while queue:
        cur_v = queue.popleft()
        nv_list = vertex_dict[cur_v]
        for nv in nv_list:
            if not visited[nv]:
                queue.append(nv)
                visited[nv] = True
    return visited

com = int(input())
node = int(input())
visited = [False] * (com + 1)
vertex_dict = {}
for i in range(1, com+1):
    vertex_dict[i] = []

for i in range(node):
    a, b = map(int, input().split())
    vertex_dict[a].append(b)
    vertex_dict[b].append(a)

visited = bfs(visited, vertex_dict)
count = 0
for i in range(1, com + 1):
    if i != 1 and visited[i]:
        count += 1
print(count)