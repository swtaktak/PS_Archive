import sys
import heapq
input = sys.stdin.readline

def prim(start):
    q = []
    heapq.heappush(q, [0, start]) # cost, v
    sum_w = 0
    
    while q:
        cur_w, cur_v = heapq.heappop(q)
        if not visited[cur_v]:
            visited[cur_v] = True
            sum_w += cur_w
            nv_list = graph[cur_v]
            for nv in nv_list:
                next_v, next_w = nv[0], nv[1]
                if not visited[next_v]:
                    heapq.heappush(q, [next_w, next_v])
    return sum_w
    
coms = int(input())
edges = int(input())
visited = [False for _ in range(coms + 1)]
graph = [[] for _ in range(coms + 1)]
for _ in range(edges):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])
    graph[end].append([start, cost])
print(prim(1))