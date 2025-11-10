#  풀이법 - 풀로이드 와샬 (중간 - 시작 -끝 순서임에 주의!)
import sys
input = sys.stdin.readline
INF = 1e9
vertex, edge = map(int, input().split())
graph = [[INF for _ in range(vertex + 1)] for _ in range(vertex + 1)]

for _ in range(edge):
    start, end, dist = map(int, input().split())
    graph[start][end] = dist
    
for mid in range(1, vertex + 1):
    for left in range(1, vertex + 1):
        for right in range(1, vertex + 1):
            graph[left][right] = min(graph[left][right], graph[left][mid] + graph[mid][right])
            
answer = 1e9
for i in range(1, vertex + 1):
    answer = min(answer, graph[i][i])
    
if answer == 1e9:
    print(-1)
else:
    print(answer)