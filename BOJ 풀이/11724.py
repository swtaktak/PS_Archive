# 정점 / 간선  나눠진 영역의 개수를 세는 법
# vertex 1부터 돌면서, visited 넘겨주고
# 이 넘겨주는 bfs 연산 자체를 하는 행위를 
from collections import deque
import sys
def bfs(i, vertex_dict, visited):
    queue = deque()
    visited[i] = True
    queue.append(i)
    while queue:
        cur_v = queue.pop()
        next_list = vertex_dict[cur_v]
        for nv in next_list:
            if not visited[nv]:
                visited[nv] = True
                queue.append(nv)
    return visited

vertex, edge = map(int, input().split())
visited = [False] * (vertex+1)
vertex_dict = {}
for i in range(1, vertex+1):
    vertex_dict[i] = []

for i in range(edge):
    a, b = map(int, sys.stdin.readline().split())
    vertex_dict[a].append(b)
    vertex_dict[b].append(a)

count = 0
# bfs 단계
for i in range(1, vertex+1):
    if not visited[i]:
        count += 1
        visited = bfs(i, vertex_dict, visited)
print(count)