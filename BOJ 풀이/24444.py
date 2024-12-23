import sys
from collections import deque
input = sys.stdin.readline

vertex, edge, start = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]
visited = [0 for _ in range(vertex + 1)]

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
q = deque()
q.append(start)
cur_turn = 1
visited[start] = 1
while q:
    cur_v = q.popleft()
    nv_list = graph[cur_v]
    nv_list.sort()
    for nv in nv_list:
        if visited[nv] == 0:
            cur_turn += 1
            visited[nv] = cur_turn
            q.append(nv)

for i in range(1, vertex + 1):
    print(visited[i])