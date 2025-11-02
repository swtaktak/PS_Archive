# Prim Algorithm
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
def prim_algorithm(start):
    q = []
    heapq.heappush(q, (0, start))
    sum_w = 0
    while q:
        cur_w, cur_v = heapq.heappop(q)
        if not visited[cur_v]:
            visited[cur_v] = True
            sum_w += cur_w
            nv_list = graph[cur_v]
            for nv in nv_list:
                if not visited[nv[0]]:
                    heapq.heappush(q, (nv[1], nv[0]))
    return sum_w
        

while True:
    vertex, edge = map(int, input().split())

    if vertex == 0 and edge == 0:
        break
    else:
        graph = [[] for _ in range(vertex)]
        visited = [False for _ in range(vertex)]
        cost_sum = 0
        
        for _ in range(edge):
            start, end, cost = map(int, input().split())
            graph[start].append([end, cost])
            graph[end].append([start, cost])
            cost_sum += cost
            
        max_reduce = prim_algorithm(0)
        print(cost_sum - max_reduce)