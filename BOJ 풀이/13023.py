import sys
input = sys.stdin.readline

vertex, edge = map(int, input().split())
graph = [[] for _ in range(vertex)]

def dfs(start, depth):
    global flag
    if depth == 5:
        flag = True
        return
    for nv in graph[start]:
        if not visited[nv]:
            visited[nv] = True
            dfs(nv, depth + 1)
            visited[nv] = False


for _ in range(edge):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


flag = False
for i in range(vertex):
    visited = [False] * vertex
    visited[i] = True
    dfs(i, 1)
    if flag:
        break
    
if flag:
    print(1)
else:
    print(0)