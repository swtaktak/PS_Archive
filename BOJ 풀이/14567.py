import sys
from collections import deque
input = sys.stdin.readline

vertex, edge = map(int, input().split())
indegree_list = [0] * (vertex + 1)
graph = [[] for _ in range(vertex + 1)]
answer_list = [1] * (vertex + 1)

for _ in range(edge):
    left, right = map(int, input().split())
    indegree_list[right] += 1
    graph[left].append(right)

q = deque()
for i in range(1, vertex + 1):
    if indegree_list[i] == 0:
        q.append(i)

while q:
    cur_v = q.popleft()
    nv_list = graph[cur_v]
    for nv in nv_list:
        indegree_list[nv] -= 1
        if indegree_list[nv] == 0:
            answer_list[nv] = answer_list[cur_v] + 1
            q.append(nv)

for a in answer_list[1:]:
    print(a, end = " ")