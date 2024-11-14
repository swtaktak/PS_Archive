import sys
from collections import deque
input = sys.stdin.readline
node = int(input())
tree = [[] for _ in range (node + 1)]

for _ in range(1, node):
    start, end, cost = map(int, input().split())
    tree[start].append([end, cost])
    tree[end].append([start, cost])

def bfs(start, tree):
    dist = [-1] * (node + 1)
    queue = deque()
    queue.append(start)
    dist[start] = 0
    
    while queue:
        cur_v = queue.pop()
        next_list = tree[cur_v]
        for next_v, next_dist in next_list:
            if dist[next_v] == -1:
                dist[next_v] = next_dist + dist[cur_v]
                queue.append(next_v)
    return dist
                # 단계 1 : 1번 노드에서 연결된 거리를 모두 구한다. bfs로
dist_list = bfs(1, tree)
# 단계 2 : 가장 먼 노드는 지름의 위치가 확정된다. 거기서 가장 먼 노드까지의 거리를 또 구한다.
diameter_start_pos = dist_list.index(max(dist_list))
print(max(bfs(diameter_start_pos, tree)))