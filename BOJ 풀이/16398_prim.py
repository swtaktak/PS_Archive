# MST 복습 - Prim 버전
# Prim 버전의 핵심 : heap을 사용한다.
# 연결된 거중 그리디하게 사이클 안생기게 가장 작은 거를 연결
# 여기서는 힙을 통해 선을 결정한다.

import sys
import heapq
input = sys.stdin.readline

def prim(start):
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, start)) # 비용, 현재 점
    sum_w = 0
    while q:
        cur_w, cur_v = heapq.heappop(q)
        # 사이클이 연결 안되는 최소 코스트 간선인가?
        if not visited[cur_v]:
            visited[cur_v] = True
            sum_w += cur_w
            # 다음에 넣을 후보를 판단한다. 사이클이면 제외, 안되는걸 넣는다.
            # 현재 점에서 연결된거만 찾으면 그만이므로
            nv_list = graph[cur_v]
            for nv in nv_list:
                cur_nv, cur_nv_cost = nv[0], nv[1]
                if not visited[cur_nv]:
                    heapq.heappush(q, (cur_nv_cost, cur_nv))
    return sum_w
        

N = int(input())
graph= [[] for _ in range(N)]
visited = [False for _ in range(N)]

for i in range(N):
    cur_cost = list(map(int, input().split()))
    
    for j in range(N):
        if cur_cost[j] > 0:
            # 도착점, 비용
            graph[i].append((j, cur_cost[j]))

answer = prim(0)
print(answer)