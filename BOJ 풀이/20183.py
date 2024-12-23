import sys
import heapq
input = sys.stdin.readline
INF = 1e15

def dijkstra(cost_limit):
    # 해당 코스트 이하의 간선만 추가하는 다익스트라로 변경하여 풀이.
    cost_list = [INF for _ in range(vertex + 1)]
    cost_list[start] = 0
    
    q = []
    heapq.heappush(q, [0, start]) # 비용, 점 / 비용으로 정렬
    while q:
        cur_cost, cur_v = heapq.heappop(q)
        if cost_list[cur_v] < cur_cost:
            continue
        for next_v, next_cost in graph[cur_v]:
            # 한 번에 쓸 수 있는 최대 한계인 경우만만
            if next_cost <= cost_limit:
                new_cost = next_cost + cur_cost
                if new_cost < cost_list[next_v]:
                    cost_list[next_v] = new_cost
                    heapq.heappush(q, [new_cost, next_v])
    if cost_list[end] <= max_money:
        return True
    else:
        return False
                
vertex, edge, start, end, max_money = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]
max_road_cost = 0
for _ in range(edge):
    a, b, cur_cost = map(int, input().split())
    max_road_cost = max(cur_cost, max_road_cost)
    graph[a].append([b, cur_cost])
    graph[b].append([a, cur_cost])

left = 0
right = max_road_cost
answer = INF
while left <= right:
    # 이거를 수치심의 한계치로 둘거임임
    suchi = (left + right) // 2
    if dijkstra(suchi):
        answer = min(answer, suchi)
        right = suchi - 1
    else:
        left = suchi + 1
if answer == INF:
    print(-1)
else:
    print(answer)