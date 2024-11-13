# 다익스트라 이해하기
import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
city = int(input())
bus = int(input())
bus_line = [[] for _ in range(city + 1)] # 각 시작점 별로 도착점과 비용만 담으면 됨, city가 범위에 주의.
cost_list = [INF for _ in range(city + 1)]

for _ in range(bus):
    start, end, cost = map(int, input().split())
    bus_line[start].append((end, cost))

start_city, end_city = map(int, input().split())
cost_list[start_city] = 0

def dijkstra(start):
    q = []
    heapq.heapify(q)
    
    heapq.heappush(q, (0, start)) # 비용, 노드 번호,  시작점의 비용은 0!
    while q:
        cur_cost, cur_node = heapq.heappop(q) # 가장 최소의 비용을 가진 애를 pop
        if cost_list[cur_node] < cur_cost:
            # 이미 기존의 비용이, 현재의 비용보다 작다면, 이미 비용 판단을 했던 애라, 처리 스킵.
            continue
        
        # 현재 노드에서 연결된 다음 노드들에 대한 비용 판단
        for next_v, next_cost in bus_line[cur_node]:
            new_cost = cur_cost + next_cost
            if new_cost < cost_list[next_v]: # 다음 노드로 가는 비용이 더 적다면
                cost_list[next_v] = new_cost
                heapq.heappush(q, (new_cost, next_v)) # 다음 비용과 지점을 입력

dijkstra(start_city)
print(cost_list[end_city])