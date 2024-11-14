import sys
from collections import deque
input = sys.stdin.readline
vertex = int(input())
tree = [[] for _ in range (vertex + 1)]

for _ in range(vertex):
    cur_list = list(map(int, input().split()))
    cur_v = cur_list[0]
    for j in range(1, len(cur_list)-1, 2):
        child, dist = cur_list[j], cur_list[j+1]
        tree[cur_v].append([child, dist])


def bfs(start, tree):
    dist = [-1] * (vertex + 1)
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