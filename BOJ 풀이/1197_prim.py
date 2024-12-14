# Prim Algorithm
# 하나의 정점을 정한 뒤, 정점에 연결된 최소 가중치를 선택한다.
# 남은 정점에 연결된 가장 최소 가중치를 꾸준히 선택해 나간다.
# 다만, 한 번 방문한 정점은 두 번 다시 방문하지 않는다 = 이는 cycle 방지.
# 이렇게 하여, 모든 정점을 방문하면 알고리즘을 종료
# 힙을 사용하면 O(ElogV) # 간선이 많을 때는 프림이 유리하다.
import sys
import heapq
input = sys.stdin.readline

def prim(start):
    q = []
    heapq.heappush(q, (0, start)) # 최초 비용과 시작점 넣음
    sum_w = 0 # 가중치의 합
    while q:
        cur_w, cur_v = heapq.heappop(q)
        if not visited[cur_v]:
            visited[cur_v] = True
            sum_w += cur_w
            nv_list = graph[cur_v]
            for nv in nv_list:
                cur_nv, cur_next_cost = nv[0], nv[1]
                # 방문한 적 없는 점에 연결된 신규 간선일 경우 모두 추가해버린다.
                if not visited[cur_nv]:
                    heapq.heappush(q, (cur_next_cost, cur_nv))
    return sum_w
vertex, edge = map(int, input().split())
visited = [False] * (vertex + 1)
graph = [[] for _ in range(vertex + 1)]

for _ in range(edge):
    start, end, cur_cost = map(int, input().split())
    graph[start].append([end, cur_cost])
    graph[end].append([start, cur_cost])

answer = prim(1)

print(answer)

