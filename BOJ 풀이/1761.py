import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    left, right, dist = map(int, input().split())
    tree[left].append((right, dist))
    tree[right].append((left, dist))
    
MAX_DEPTH = N.bit_length()
depth = [0 for _ in range(N + 1)]
dist = [0 for _ in range(N + 1)]
parent = [[0 for _ in range(N + 1)] for _ in range(MAX_DEPTH)]

dist[1] = 0

# 트리 초기화 및 거리 계산
def dfs_with_dist(cur_v, prev_v):
    parent[0][cur_v] = prev_v
    for next_v, next_dist in tree[cur_v]:
        if next_v == prev_v:
            continue
        depth[next_v] = depth[cur_v] + 1
        dist[next_v] = dist[cur_v] + next_dist
        dfs_with_dist(next_v, cur_v)
dfs_with_dist(1, 0)


for cur_d in range(1, MAX_DEPTH):
    for cur_v in range(1, N + 1):
        parent[cur_d][cur_v] = parent[cur_d -1][parent[cur_d-1][cur_v]]
        
def lca(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    
    depth_gap = depth[u] - depth[v]
    for cur_d in range(MAX_DEPTH):
        if depth_gap & (1 << cur_d): 
            u = parent[cur_d][u]
    
    if u == v:
        return u
    
    for cur_d in range(MAX_DEPTH -1, -1, -1):
        if parent[cur_d][u] != parent[cur_d][v]:
            u = parent[cur_d][u]
            v = parent[cur_d][v]
    return parent[0][u]


Q = int(input())
for _ in range(Q):
    u, v = map(int, input().split())
    lca_uv = lca(u, v)
    ans = dist[u] + dist[v] - 2 * dist[lca_uv]
    print(ans)