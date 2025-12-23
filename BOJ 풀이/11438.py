# LCA 2 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
tree = [[] for _ in range(N + 1)]

for _ in range(N-1):
    left, right = map(int, input().split())
    tree[left].append(right)
    tree[right].append(left)
    

MAX_DEPTH = N.bit_length()
depth = [0 for _ in range(N+1)]
# 각 노드별로 몇층에 뭐가 있나 기록한다.
parent = [[0 for _ in range(N + 1)] for _ in range(MAX_DEPTH)]


# STEP 1 : depth와 직계 부모를 채운다.
def dfs_build_depth_and_parent(cur_v, prev_v):
    parent[0][cur_v] = prev_v
    for next_v in tree[cur_v]:
        if next_v == prev_v: # 자식을 향해 가야 하는데 부모로 가버려서 패스
            continue
        depth[next_v] = depth[cur_v] + 1
        dfs_build_depth_and_parent(next_v, cur_v)

dfs_build_depth_and_parent(1, 0)

# STEP 2 : parent k단계 채우기
# 즉 k개 위 부모를 계산하자.
for cur_d in range(1, MAX_DEPTH):
    for cur_v in range(1, N + 1):
        parent[cur_d][cur_v] = parent[cur_d -1][parent[cur_d-1][cur_v]]
        
# STEP 3 : lca 알고리즘
def lca(u, v):
    # 3-1 깊이를 통과한다. 왼쪽이 더 깊은 것으로 통일하자.
    if depth[u] < depth[v]:
        u, v = v, u
    
    # 왼쪽은 올라가야 한다.
    depth_gap = depth[u] - depth[v]
    # 왼쪽을 하나하나 올리지 말고, 2진법으로 빠르게 올린다.
    for cur_d in range(MAX_DEPTH):
        if depth_gap & (1 << cur_d): # 2진수 기준으로 올라가는 코드
            u = parent[cur_d][u]
    
    # 깊이가 같아졌는데 같은 노드면 끝
    if u == v:
        return u
    
    # 깊이가 같아졌음 같이 올라가는데, 부모가 다를때까지만 올라가게 됨
    # 부모가 같다면, 굳이 안올라감.
    for cur_d in range(MAX_DEPTH -1, -1, -1):
        if parent[cur_d][u] != parent[cur_d][v]:
            u = parent[cur_d][u]
            v = parent[cur_d][v]
    # 이제 LCA 바로 밑 까지 와서 바로 위를 말하는 0번을 뱉게 됨
    return parent[0][u]

# STEP 4 : 쿼리 처리
Q = int(input())
ans = []

for _ in range(Q):
    u, v = map(int, input().split())
    ans.append(lca(u, v))

for a in ans:
    print(a)