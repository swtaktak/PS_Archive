# 플로이드 와샬 알고리즘
import sys
input = sys.stdin.readline
INF = 999999999

city = int(input())
plans = int(input())

graph = [[INF for _ in range(city)] for _ in range(city)]

# 그래프 입력
for i in range(city):
    cur_dist = list(map(int, input().split()))
    for j in range(city):
        if cur_dist[j] == 1:
            graph[i][j] = 1
        elif i == j:
            graph[i][j] = 1
# 거리 계산
for k in range(city):
    for i in range(city):
        for j in range(city):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

trip_plan = list(map(int, input().split()))

judge = True
for i in range(1, plans):
    left, right = trip_plan[i-1]-1, trip_plan[i]-1
    if graph[left][right] == INF:
        judge = False
        break

if plans == 1:
    print('YES')
elif judge:
    print('YES')
else:
    print('NO')