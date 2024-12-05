import sys
import heapq
input = sys.stdin.readline
INF = 1e15
def dijkstra(first):
    q = []
    heapq.heappush(q,(0, first)) # 비용, 시작점
    
    while q:
        cur_cost, cur_v = heapq.heappop(q)
        if cost_list[cur_v] < cur_cost:
            continue
        for next_v, next_cost in graph[cur_v]:
            if cost_list[next_v] > cost_list[cur_v] + next_cost:
                cost_list[next_v] = cost_list[cur_v] + next_cost
                heapq.heappush(q, (cost_list[next_v], next_v))

T = int(input())
for _ in range(T):
    coms, lines, first = map(int, input().split())
    cost_list = [INF] * (coms+1)
    cost_list[first] = 0
    graph = [[] for _ in range(coms + 1)]
    
    for _ in range(lines):
        start, end, cur_cost = map(int, input().split())
        graph[end].append((start, cur_cost))
        
    dijkstra(first)
    virus_com = 0
    virus_time = 0
    for i in range(1, coms + 1):
        if cost_list[i] < INF:
            virus_com += 1
            virus_time = max(virus_time, cost_list[i])
    print("%d %d" %(virus_com, virus_time))