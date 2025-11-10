import sys
import heapq
input = sys.stdin.readline
INF = 1e15
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

N = int(input())
cost_list = [INF for _ in range(N+1)]
cost_list[1] = 0

graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    start, end, dist = map(int, input().split())
    graph[start].append((end, dist))
    graph[end].append((start, dist))
popu_list = [0] + list(map(int, input().split()))

cost_list = dijkstra(1, cost_list)

# 어차피, 상행, 하행 개수가 같음은 보장된다. 개수를 센다.
cost_popu_dict = {}
for i in range(2, N+1):
    if cost_list[i] != INF:
        if (cost_list[i], popu_list[i]) not in cost_popu_dict:
            cost_popu_dict[(cost_list[i], popu_list[i])] = 1
        else:
            cost_popu_dict[(cost_list[i], popu_list[i])] += 1

#  연결성이 보장되어 있어서 1번을 제외하고 저 dict의 값에 대해 처분
answer = N - 1
dict_cnt_list = list(cost_popu_dict.values())
# 합의 제곱 - 제곱의 합으로 계산하면 된다.
sum_sq = sum(dict_cnt_list) ** 2
sq_sum = 0
for d in dict_cnt_list:
    sq_sum += (d ** 2)
    
answer += ((sum_sq - sq_sum) // 2)
print("%d %d" %(answer, answer))