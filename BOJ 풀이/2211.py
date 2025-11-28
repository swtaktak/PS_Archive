# 2211
# 기본적으로는 스패닝 트리인데, 추가하는 간선에 대한 정보를 어떻게 줄 것인가?
# 크루스칼로 풀어야 유니온 파인드 과정에서, 간선 입력이 편하다.
import sys
import heapq
input = sys.stdin.readline
INF = 10 ** 18 

def dijkstra(start_v):
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, start_v))
    
    while q:
        cur_cost, cur_v = heapq.heappop(q)
        if cur_cost > dist[cur_v]:
            continue
        
        for next_v, next_cost in graph[cur_v]:
            if dist[next_v] > dist[cur_v] + next_cost:
                dist[next_v] = dist[cur_v] + next_cost
                # Point : 갱신할 점으로 연결 바꿀거임
                parent[next_v] = cur_v
                heapq.heappush(q, (dist[next_v], next_v))
                
vertex, edge = map(int, input().split())
edges = []
graph = [[] for _ in range(vertex + 1)]

for _ in range(edge):
    left, right, cost = map(int, input().split())
    graph[left].append((right, cost))
    graph[right].append((left, cost))

dist = [INF for _ in range(vertex + 1)]
parent = [0 for _ in range(vertex + 1)]

dist[1] = 0
dijkstra(1)
print(vertex - 1)
for i in range(2, vertex + 1):
    print("%d %d" %(i, parent[i]))