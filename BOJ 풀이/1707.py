import sys
from collections import deque
input = sys.stdin.readline

def bipartite_bfs(start):
    global flag
    queue = deque()
    queue.append((start, 1)) # 시작점 / 색은 1 or 2
    color_list[start] = 1
    while queue:
        cur_v, cur_color = queue.popleft()
        for nv in graph[cur_v]:
            if color_list[nv] == 0:
                color_list[nv] = 3-cur_color
                queue.append((nv, 3-cur_color))
            else:
                if color_list[nv] == color_list[cur_v]:
                    flag = False

T = int(input())
for _ in range(T):
    vertex, edge = map(int, input().split())
    color_list = [0] * (vertex + 1) # 0이면 미방문 1, 2로 판단
    graph = [[] for _ in range(vertex + 1)]
    
    for _ in range(edge):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    flag = True
    
    for i in range(1, vertex+1):
        if color_list[i] == 0:
            bipartite_bfs(i)
    
    if flag:
        print('YES')
    else:
        print('NO')