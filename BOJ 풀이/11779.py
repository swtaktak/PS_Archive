# 복습하고 배워봅시다 - 다익스트라, 근데 경로까지 기억하기
import sys
import heapq
input = sys.stdin.readline
INF = 1e9

def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    
    while q:
        cur_cost, cur_node = heapq.heappop(q)
        if cost_list[cur_node] < cur_cost:
            continue
        
        for next_v, next_cost in graph[cur_node]:
            new_cost = cur_cost + next_cost
            if new_cost < cost_list[next_v]:
                cost_list[next_v] = new_cost
                # 갱신시에 점을 둔다.
                parent_list[next_v] = cur_node
                heapq.heappush(q, (new_cost, next_v))
    
vertex = int(input())
edge = int(input())
graph = [[] for _ in range(vertex + 1)]
cost_list = [INF for _ in range(vertex + 1)]
parent_list = [i for i in range(vertex + 1)]
for _ in range(edge):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost]) # 도착점, 비용

start, end = map(int, input().split())
cost_list[start] = 0
dijkstra(start)
print(cost_list[end])

# 경로를 구한다.
answer_path = []
cur_v = end
while True:
    answer_path.append(cur_v)
    if cur_v == parent_list[cur_v]:
        break
    cur_v = parent_list[cur_v]
print(len(answer_path))
for p in answer_path[::-1]:
    print(p, end = " ")