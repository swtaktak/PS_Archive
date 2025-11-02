import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True
    
    while q:
        cv = q.popleft()
        nv_list = graph[cv]
        for nv in nv_list:
            if not visited[nv]:
                visited[nv] = True
                q.append(nv)
                
vertex, edge = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]
visited = [False for _ in range(vertex + 1)]

for _ in range(edge):
    left, right = map(int, input().split())
    graph[left].append(right)
    graph[right].append(left)
    
component = 0
for i in range(1, vertex + 1):
    if not visited[i]:
        bfs(i)
        component += 1
print(component - 1)