# 14621
# Prim / Kruscal의 약간 응용
# Prim 버전 풀이
# 그래프 목록이 애초에 맞나, 틀리나를 판단하자.
import sys
import heapq
input = sys.stdin.readline

def prim(start):
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, start))
    sum_w = 0
    cnt = 0
    
    while q:
        cur_w, cur_v = heapq.heappop(q)
        if not visited[cur_v]:
            visited[cur_v] = True
            sum_w += cur_w
            nv_list = graph[cur_v]
            cnt += 1
            
            for nv in nv_list:
                cur_next_cost, cur_nv = nv[0], nv[1]
                if not visited[cur_nv]:
                    heapq.heappush(q, (cur_next_cost, cur_nv)) 
                               
    if cnt == school:
        return sum_w
    else:
        return -1

school, edge = map(int, input().split())
gender_list = ['nan'] + list(map(str, input().rstrip().split()))

visited = [False for _ in range(school + 1)]
graph = [[] for _ in range(school + 1)]

for _ in range(edge):
    left, right, dist = map(int, input().split())
    if gender_list[left] != gender_list[right]:
        graph[left].append((dist, right))
        graph[right].append((dist, left))

answer = prim(1)
print(answer)