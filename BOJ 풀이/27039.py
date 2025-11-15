import sys
input = sys.stdin.readline
INF = 10 ** 9
cow, farm, edge = map(int, input().split())
cow_list = []
graph = [[INF for _ in range(farm + 1)] for _ in range(farm + 1)]

for _ in range(cow):
    cur_cow = int(input())
    cow_list.append(cur_cow)

for _ in range(edge):
    left, right, dist = map(int, input().split())
    graph[left][right] = dist
    graph[right][left] = dist

for i in range(1, farm + 1):
    graph[i][i] = 0
    
# 플로이드 와샬.
for mid in range(1, farm + 1):
    for left in range(1, farm + 1):
        for right in range(1, farm + 1):
            graph[left][right] = min(graph[left][right], graph[left][mid] + graph[mid][right])


ans = INF
for cur_farm in range(1, farm + 1):
    cur_cost = 0
    for cur_cow in cow_list:
        cur_cost += graph[cur_cow][cur_farm]
    ans = min(ans, cur_cost)

print(ans)