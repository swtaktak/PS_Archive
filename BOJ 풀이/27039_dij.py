import sys
import heapq
input = sys.stdin.readline

INF = 10 ** 9

def dijkstra(start_v):
    global cost_list
    
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, start_v))
    
    while q:
        cur_cost, cur_v = heapq.heappop(q)
        if cost_list[cur_v] < cur_cost:
            continue
        for next_v, next_cost in graph[cur_v]:
            new_cost = cur_cost + next_cost
            if new_cost < cost_list[next_v]:
                cost_list[next_v] = new_cost
                heapq.heappush(q, (new_cost, next_v))
                
cow, farm, edge = map(int, input().split())
cow_list = []
graph = [[] for _ in range(farm + 1)]

for _ in range(cow):
    cur_cow = int(input())
    cow_list.append(cur_cow)

for _ in range(edge):
    left, right, dist = map(int, input().split())
    graph[left].append((right, dist))
    graph[right].append((left, dist))

ans = 1e9
for start_farm in range(1, farm + 1):
    cost_list = [0] + [INF for _ in range(farm)]
    cost_list[start_farm] = 0
    
    dijkstra(start_farm)
    
    cur_ans = 0
    for cur_cow in cow_list:
        cur_ans += (cost_list[cur_cow])
    ans = min(cur_ans, ans)
print(ans)