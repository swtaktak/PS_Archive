import sys 
import heapq

student, road, party_place = map(int, input().split())
INF = 1e9
road_list = [[] for _ in range(student + 1)]
for _ in range(road):
    start, end, time = map(int, input().split())
    road_list[start].append((end, time))

def dijkstra(start):
    cur_cost_list = [INF for _ in range(student + 1)]
    cur_cost_list[start] = 0
    
    q = []
    heapq.heapify(q)
    
    heapq.heappush(q, (start, 0)) # 점, 비용
    
    while q:
        cur_v, cur_cost = heapq.heappop(q)
        if cur_cost > cur_cost_list[cur_v]:
            continue
        
        for next_v, next_cost in road_list[cur_v]:
            new_cost = cur_cost + next_cost
            if cur_cost_list[next_v] > new_cost:
                cur_cost_list[next_v] = new_cost
                heapq.heappush(q, (next_v, new_cost))
    return cur_cost_list

# 우선 돌아가고, 나머지를 계산하자.
total_time_list = dijkstra(party_place)

for i in range(1, student + 1):
    if i == party_place:
        pass
    else:
        cur_time = dijkstra(i)[party_place]
        total_time_list[i] += cur_time
print(max(total_time_list[1:]))