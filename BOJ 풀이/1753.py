# 다익스트라 직접 해보기
import sys
import heapq
input = sys.stdin.readline

vertex, edge = map(int, input().split())
start_v = int(input()) # 시작점
INF = int(1e18)
cost_list = [INF for _ in range(vertex + 1)]
graph_list = [[] for _ in range(vertex + 1)]
cost_list[start_v] = 0
for _ in range(edge):
    start, end, cost = map(int, input().split())
    graph_list[start].append((end, cost)) # 연결된 곳 까지의 비용을 입력한다.
    
def dijkstra(start_v):
    q = []
    heapq.heapify(q)
    
    heapq.heappush(q, (0, start_v)) # 비용과 출발지점
    
    while q:
        cur_cost, cur_v = heapq.heappop(q)
        # 만일 비용이 더 크다면, 볼 필요가 없다. 방문 체크용임
        if cost_list[cur_v] < cur_cost:
            continue
        
        for next_v, next_cost in graph_list[cur_v]:
            # 그리디하게 비교한다. 최저 비용을 뽑아왔다. 현재 추가 선과 비교해서 더 적으면 추가.
            new_cost = cur_cost + next_cost
            if new_cost < cost_list[next_v]:
                cost_list[next_v] = new_cost
                heapq.heappush(q, (new_cost, next_v))
dijkstra(start_v)
for c in cost_list[1:]:
    if c == INF:
        print('INF')
    else:
        print(c)