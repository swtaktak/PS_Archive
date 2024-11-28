import sys
from collections import deque
input = sys.stdin.readline

node, t_case = map(int, input().split())
node_list = [[] for _ in range(node + 1)]
for _ in range(1, node):
    start, end, dist = map(int, input().split())
    node_list[start].append((end, dist))
    node_list[end].append((start, dist))

def bfs(start, end):
    cost_list = [0] * (node + 1)
    visited = [False] * (node + 1)
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        cur_node = queue.popleft()
        next_infos = node_list[cur_node]
        for next_info in next_infos:
            next_node = next_info[0]
            next_cost = next_info[1]
            if not visited[next_node]:
                cost_list[next_node] = cost_list[cur_node] + next_cost
                visited[next_node] = True
                queue.append(next_node)
    return cost_list[end]

for _ in range(t_case):
    start, end = map(int, input().split())
    print(bfs(start, end))