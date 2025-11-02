import sys
input = sys.stdin.readline

mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]  

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  
    return parent[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    
    if root_x != root_y:
        parent[root_y] = root_x 

N, Q = map(int, input().split())
col_list = list(map(int, input().split()))
row_list = list(map(int, input().split()))

parent = [i for i in range(N * N)]  

for r in range(N):
    for c in range(N):
        if (col_list[r] + row_list[c]) % 2 == 0:  
            curr = r * N + c  # 1D 인덱스
            for dr, dc in mv_list:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if (col_list[nr] + row_list[nc]) % 2 == 0:
                        union(curr, nr * N + nc)

for _ in range(Q):
    ra, ca, rb, cb = map(int, input().split())
    if find((ra-1) * N + (ca-1)) == find((rb-1) * N + (cb-1)):  
        print("YES")
    else:
        print("NO")
