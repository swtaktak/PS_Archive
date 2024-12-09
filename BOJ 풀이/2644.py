import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    dist[start] = 0
    
    while q:
        cur_v = q.popleft()
        next_v = tree[cur_v]
        for nv in next_v:
            if dist[nv] == -1:
                dist[nv] = dist[cur_v] + 1
                q.append(nv)
                if nv == ans_e:
                    break

vertex = int(input())
ans_s, ans_e = map(int, input().split())
edge = int(input())
tree = [[] for _ in range(vertex + 1)]

for _ in range(edge):
    start, end = map(int, input().split())
    tree[start].append(end)
    tree[end].append(start)

dist = [-1] * (vertex + 1)
bfs(ans_s)
print(dist[ans_e])