import sys
from collections import deque
def dfs(cur_v, vertex_dict, visited_dfs):
    global dfs_result
    if len(dfs_result) == vertex:
        return
    else:
        nv_list = sorted(vertex_dict[cur_v])
        for nv in nv_list:
            if not visited_dfs[nv]:
                dfs_result.append(nv)
                visited_dfs[nv] = True
                dfs(nv, vertex_dict, visited_dfs)
        return
def bfs(start, vertex_dict, visited_bfs):
    global bfs_result
    queue = deque()
    queue.append(start)
    visited_bfs[start] = True
    while queue:
        cur_v = queue.popleft()
        nv_list = sorted(vertex_dict[cur_v])
        for nv in nv_list:
            if not visited_bfs[nv]:
                bfs_result.append(nv)
                visited_bfs[nv] = True
                queue.append(nv)

input = sys.stdin.readline
vertex, edge, start_v = map(int, input().split())
vertex_dict = {}
for i in range(1, vertex+1):
    vertex_dict[i] = []
for _ in range(edge):
    x, y = map(int, input().split())
    vertex_dict[x].append(y)
    vertex_dict[y].append(x)

visited_dfs = [False] * (vertex+1)
visited_bfs = [False] * (vertex+1)
visited_dfs[start_v] = True
dfs_result = [start_v]
bfs_result = [start_v]
dfs(start_v, vertex_dict, visited_dfs)
bfs(start_v, vertex_dict, visited_bfs)

for i in range(len(dfs_result)):
    print(dfs_result[i], end = " ")
print()
        
for i in range(len(bfs_result)):
    print(bfs_result[i], end = " ")
