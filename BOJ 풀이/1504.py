# 1번에서 N번 가기, 단 a, b는 무조건 지나시오!
# 1-> a -> b -> N   vs  1-> b -> a -> N
# 1번의 다익스트라, a번의 다익스트라,  b번의 다익스트라를 만들면 된다.
import sys
import heapq
input = sys.stdin.readline
INF = (1e18)
vertex, edge = map(int, input().split())
cost_list_1 = [INF] * (vertex + 1)
cost_list_a = [INF] * (vertex + 1)
cost_list_b = [INF] * (vertex + 1)
graph = [[] for _ in range (vertex + 1)]

for _ in range(edge):
    # 이번에는 양방향임에 주의
    left, right, cost = map(int, input().split())
    graph[left].append((right, cost))
    graph[right].append((left, cost))
    
mand_v_a, mand_v_b = map(int, input().split())

def dijkstra(start, cost_list):
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, start)) # 비용, 시작점
    cost_list[start] = 0
    
    while q:
        cur_cost, cur_v = heapq.heappop(q)
        # 힙에서 나온 비용이, 현재 비용보다 크다면 더 작아질 수 없어서 방문 이미 한거임.
        if cost_list[cur_v] < cur_cost:
            continue
        for next_v, next_cost in graph[cur_v]:
            new_cost = cur_cost + next_cost
            # 현재 비용이 지금까지 저장된 비용보다 적다면?
            if new_cost < cost_list[next_v]:
                cost_list[next_v] = new_cost
                heapq.heappush(q, (new_cost, next_v))
    return cost_list

cost_list_1 = dijkstra(1, cost_list_1)
cost_list_a = dijkstra(mand_v_a, cost_list_a)
cost_list_b = dijkstra(mand_v_b, cost_list_b)

route_a = cost_list_1[mand_v_a] + cost_list_a[mand_v_b] + cost_list_b[vertex]
route_b = cost_list_1[mand_v_b] + cost_list_b[mand_v_a] + cost_list_a[vertex]
if route_a >= INF and route_b >= INF:
    print(-1)
else:
    print(min(route_a, route_b))