import sys
from collections import deque
input = sys.stdin.readline
# 트리를 탐색해서. 지운 노드에서 방문 가능한걸 방문한다.
# 방문하지 않은 것 중, 자식이 없는 애들을 모두 가져온다.

vertex = int(input())
visited = [False for _ in range(vertex)]
parent_list = list(map(int, input().split()))
graph = [[] for _ in range(vertex)]
for i in range(0, vertex):
    parent = parent_list[i]
    if parent == -1:
        root = i
    else:
        graph[parent].append(i)

del_node = int(input())
visited[del_node] = True
q = deque()
q.append(del_node)
while q:
    cur_v = q.popleft()
    nv_list = graph[cur_v]
    for nv in nv_list:
        if not visited[nv]:
            visited[nv] = True
            q.append(nv)
answer = 0
for i in range(vertex):
    if not visited[i]:
        if len(graph[i]) == 0 or graph[i] == [del_node]:
            answer += 1
print(answer)