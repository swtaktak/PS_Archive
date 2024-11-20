import sys
input = sys.stdin.readline

INF = 1e18
area_num, move_lim, road_num = map(int, input().split())
# 지역별로 얻을 수 있는 아이템 개수
value_list = list(map(int, input().split()))
value_list.insert(0, 0)

graph = [[INF for _ in range(area_num + 1)] for _ in range(area_num + 1)]
for _ in range(road_num):
    start, end, length = map(int, input().split())
    graph[start][end] = length
    graph[end][start] = length

for i in range(area_num+1):
    graph[i][i] = 0

# 플로이드-워셜 얄고리즘으로 거리 데이터를 모두 받아오자.
# k 를 거쳐오면 좋을까?
for k in range(area_num + 1):
    for start in range(area_num + 1):
        for end in range(area_num + 1):
            graph[start][end] = min(graph[start][end], graph[start][k] + graph[k][end])
print(graph)
max_item_list = [0] * (area_num + 1)
for i in range(1, area_num+1):
    cur_area_start_time = graph[i]
    for j in range(len(cur_area_start_time)):
        if cur_area_start_time[j] <= move_lim:
            max_item_list[i] += value_list[j]
print(max(max_item_list))