# solution (1) dijkstra로 풀어 보기. 하나의 점에서 거리 구하기.
# Time complexity: VlogE
# 특징점 : 음의 가치에서는 사용 불가!

import sys
import heapq
input = sys.stdin.readline

INF = 1e12
vertex = int(input())
edge = int(input())
vertex_list = [[] for _ in range (vertex + 1)]


for _ in range(edge):
    start, end, cost = map(int, input().split())
    vertex_list[start].append((end, cost))

# 그리디 알고리즘, 가장 최저 비용 선을 추가한다.
def dijkstra(start, cost_list):
    q = []
    heapq.heapify(q)
    
    heapq.heappush(q, (0, start)) # cost, 시작점
    
    while q:
        cur_cost, cur_v = heapq.heappop(q)
        
        # 방문 처리임 이미 비용을 처리한 꼭지점인데... 더 크다면... 굳이?
        if cur_cost > cost_list[cur_v]:
            continue
        
        for next_v, next_cost in vertex_list[cur_v]:
            new_cost = cur_cost + next_cost
            # 더 적은 비용일때만 갱신하고, 그 점을 넣어
            if new_cost < cost_list[next_v]:
                cost_list[next_v] = new_cost
                heapq.heappush(q, (new_cost, next_v))
    return cost_list

for i in range(1, vertex + 1):
    cost_list = [INF] * (vertex + 1)
    cost_list[i] = 0
    cost_list = dijkstra(i, cost_list)[1:]
    for i in range(len(cost_list)):
        if cost_list[i] == INF:
            cost_list[i] = 0
        print(cost_list[i], end = ' ')
    print()