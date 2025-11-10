# 이걸 다익스트라로 풀어보자.
import sys
import heapq
def dijkstra(start_v, cost_list):
    q = []
    heapq.heapify(q)
    
    heapq.heappush(q, (0, start_v))
    while q:
        cur_cost, cur_v = heapq.heappop(q)
        # 만일 비용이 더 크다면, 볼 필요가 없다. 방문 체크용임
        if cost_list[cur_v] < cur_cost:
            continue
        
        for next_v, next_cost in graph[cur_v]:
            # 그리디하게 비교한다. 최저 비용을 뽑아왔다. 현재 추가 선과 비교해서 더 적으면 추가.
            new_cost = cur_cost + next_cost
            if new_cost < cost_list[next_v]:
                cost_list[next_v] = new_cost
                heapq.heappush(q, (new_cost, next_v))
    return cost_list


input = sys.stdin.readline
INF = 1e9
vertex, edge = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]

for _ in range(edge):
    start, end, dist = map(int, input().split())
    graph[start].append((end, dist))
    
answer_list = [INF for _ in range(vertex + 1)]


for i in range(1, vertex + 1):
    cost_list = [INF for _ in range(vertex + 1)]
    cost_list = dijkstra(i, cost_list)
    
    answer_list[i] = cost_list[i]

answer = min(answer_list)
if answer == INF:
    print(-1)
else:
    print(answer)
