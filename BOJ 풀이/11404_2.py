# solution (2) 플로이드 워셜 알고리즘(Floyd-Warshall)로 풀어보기.
# 댜익스트라와의 차이점 : 모든 노드에서 다른 모든 노드 까지의 최단 경로를 한번에 모두 계산한다.
# 다익스트라는 그리디, 플로이드 워셜 알고리즘은 DP
# 기본 : Dab = in(Dab, Dak + Dkb)

import sys
input = sys.stdin.readline
vertex = int(input())
edge = int(input())
INF = 1e12
graph = [[INF for _ in range(vertex + 1)] for _ in range(vertex + 1)]

# step 1. 자기 자신으로 가는 비용은 0으로 초기화 해야함
for a in range(1, vertex+1):
    graph[a][a] = 0

# step 2. a에서 b로 가는 cost를 계산할 거임. row가  출발점, col이 도착점 기준이 된다.
# 이렇게 넣으면, 선이 없는 부분은 inf가 된다.
for _ in range(edge):
    start, end, cost = map(int, input().split())
    # 주의사항, 최소값이 아닐 수도 있어서 최소값 갱신 필요
    graph[start][end] = min(cost, graph[start][end])

# k를 거쳐 가면 더 최저가 될까? 를 dp로 풀기.
for k in range(1, vertex+1):
    for start in range(1, vertex+1):
        for end in range(1, vertex+1):
            graph[start][end] = min(graph[start][end], graph[start][k] + graph[k][end])

# 최종 출력 파트
for a in range(1, vertex+1):
    for b in range(1, vertex+1):
        if graph[a][b] == INF:
            print(0, end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()