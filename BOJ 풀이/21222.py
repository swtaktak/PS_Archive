import sys
import heapq
input = sys.stdin.readline
INF = 10**15


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 저비용 우선 정렬
    
    while q:
        cur_cost, cur_v = heapq.heappop(q)
        
        if cost_list[cur_v] < cur_cost:
            continue
        
        for next_v, next_cost in graph[cur_v]:
            new_cost = next_cost + cur_cost
            if new_cost < cost_list[next_v]:
                cost_list[next_v] = new_cost
                heapq.heappush(q, (new_cost, next_v))

word_graph = {}
word_to_idx = {}
cur_idx = 0
edge_list = []
words, edges = map(int, input().split())
for _ in range(edges):
    start, end, cost = map(str, input().rstrip().split())
    cost = int(cost)
    if start not in word_to_idx:
        word_to_idx[start] = cur_idx
        cur_idx += 1
    if end not in word_to_idx:
        word_to_idx[end] = cur_idx
        cur_idx += 1
    edge_list.append([start, end, cost])
# 즉, cur_idx가 전체 들어오는 단어의 개수
graph = [[] for _ in range(cur_idx)]

for cur_e in edge_list:
    start = cur_e[0]
    end = cur_e[1]
    cost = cur_e[2]
    s_idx = word_to_idx[start]
    e_idx = word_to_idx[end]
    graph[s_idx].append((e_idx, cost))

q = int(input())
for _ in range(q):
    start, end = map(str, input().rstrip().split())
    s_idx = word_to_idx[start]
    e_idx = word_to_idx[end]
    cost_list = [INF] * cur_idx
    cost_list[s_idx] = 0
    dijkstra(s_idx)
    if cost_list[e_idx] == INF:
        print('Roger')
    else:
        print(cost_list[e_idx])