import sys
import heapq
input = sys.stdin.readline

def get_dist(l, r):
    dx = r[0] - l[0]
    dy = r[1] - l[1]
    return (dx**2 + dy**2) ** 0.5

def prim(start):
    q = []
    heapq.heappush(q, (0, start)) # dist, vertex
    sum_w = 0
    while q:
        cur_dist, cur_v = heapq.heappop(q)
        if not visited[cur_v]:
            visited[cur_v] = True
            sum_w += cur_dist
            for nv in graph[cur_v]:
                next_v, next_dist = nv[0], nv[1]
                if not visited[next_v]:
                    heapq.heappush(q, (next_dist, next_v))
    return sum_w
N = int(input())
coords = []
for _ in range(N):
    cx, cy = map(float, input().split())
    coords.append([cx, cy])

graph = [[] for _ in range(N)]
visited = [False] * N
for i in range(N-1):
    for j in range(i+1, N):
        l, r = coords[i], coords[j]
        cur_dist = get_dist(l, r)
        graph[i].append((j, cur_dist))
        graph[j].append((i, cur_dist))
        
answer = prim(0)
print(answer)