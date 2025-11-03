# 다익스트라 복습 문제
# 그냥 대놓고 다익스트라 기본 형태

import sys
import heapq

input = sys.stdin.readline

vertex, edge = map(int, input().split())
# 시작점 1로 고정, 도착점 N으로 고정
INF = 1e9

cost_list = [INF for _ in range(vertex + 1)]
graph_list = [[] for _ in range(vertex + 1)]
# 출발점의 비용은 0이므로.
cost_list[1] = 0

for _ in range(edge):
    # 양방향 그래프이므로 양쪽에 추가
    start, end, cost = map(int, input().split())
    graph_list[start].append((end, cost))
    graph_list[end].append((start, cost))
    
def dijkstra(start_v):
    q = []
    heapq.heapify(q)
    
    heapq.heappush(q, (0, start_v)) # 비용과 출발지점 추가.
    
    while q:
        cur_cost, cur_v = heapq.heappop(q)
        
        if cost_list[cur_v] < cur_cost:
            continue
        
        for next_v, next_cost in graph_list[cur_v]:
            new_cost = cur_cost + next_cost
            if new_cost < cost_list[next_v]:
                cost_list[next_v] = new_cost
                heapq.heappush(q, (new_cost, next_v))

dijkstra(1)
print(cost_list[-1])