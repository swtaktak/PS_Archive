import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, visited, vertex_dict):
    queue = deque()
    queue.append(start)
    
    while queue:
        cur_v = queue.popleft()
        nv_list = vertex_dict[cur_v]
        for nv in nv_list:
            if visited[nv] == 0:
                visited[nv] = 1
                queue.append(nv)
    return visited

vertex = int(input())
vertex_dict = {}
for i in range(0, vertex):
    vertex_dict[i] = []
    cur_list = list(map(int, input().split()))
    for j in range(len(cur_list)):
        if cur_list[j] == 1:
            vertex_dict[i].append(j)

for i in range(0, vertex):
    visited = [0] * vertex
    visited = bfs(i, visited, vertex_dict)
    for v in visited:
        print(v, end = " ")
    if i < vertex-1:
        print()