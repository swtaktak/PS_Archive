import sys
input = sys.stdin.readline
INF = 1e9
vertex, edge = map(int, input().split())
graph = [[INF for _ in range(vertex + 1)] for _ in range(vertex + 1)]
for i in range(1, vertex + 1):
    graph[i][i] = 0
    
for _ in range(edge):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1
    
for k in range(1, vertex + 1):
    for i in range(1, vertex + 1):
        for j in range(1, vertex + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_cost = INF
ans_l = 0
ans_r = 0
for first in range(1, vertex):
    for second in range(first + 1, vertex + 1):
        cur_cost = 0
        for i in range(1, vertex+1):
            cur_cost += min(graph[first][i], graph[second][i])
        # 왕복이니까
        cur_cost *= 2
        
        if min_cost > cur_cost:
            ans_l = first
            ans_r = second
            min_cost = cur_cost
print("%d %d %d" %(ans_l, ans_r, min_cost))