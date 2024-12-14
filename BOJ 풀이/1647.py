# 최소 스패닝 트리에서... 가장 큰 거 하나 빼면 해결
# 간선이 100만개로 너무 많다.  프림으로 푼다.
import sys
import heapq
input = sys.stdin.readline

def prim(start):
    max_cost = 0 # 추가 간선 중 가장 큰거 뺄거임
    sum_w = 0 # 가치 합
    q = []
    heapq.heappush(q, (0, start)) # w, v
    while q:
        cur_w, cur_v = heapq.heappop(q)
        if not visited[cur_v]:
            max_cost = max(max_cost, cur_w)
            sum_w += cur_w
            visited[cur_v] = True
            nv_list = graph[cur_v]
            for nv in nv_list:
                next_v, next_cost = nv[0], nv[1]
                if not visited[next_v]:
                    heapq.heappush(q, (next_cost, next_v))
    return sum_w - max_cost

vertex, edge = map(int, input().split())
visited = [False for _ in range(vertex + 1)]
graph = [[] for _ in range(vertex + 1)]

for _ in range(edge):
    start, end, cur_cost = map(int, input().split())
    graph[start].append([end, cur_cost])
    graph[end].append([start, cur_cost])
answer = prim(1)
print(answer)