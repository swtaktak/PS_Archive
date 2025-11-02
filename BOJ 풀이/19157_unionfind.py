import sys
input = sys.stdin.readline

mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]  

def find(r, c):
    if parent[r][c] != (r, c):  
        parent[r][c] = find(parent[r][c][0], parent[r][c][1]) 
    return parent[r][c]

def union(r1, c1, r2, c2):
    root1 = find(r1, c1)
    root2 = find(r2, c2)

    if root1 != root2: 
        parent[root2[0]][root2[1]] = root1

N, Q = map(int, input().split())
col_list = list(map(int, input().split()))
row_list = list(map(int, input().split()))
parent = [[(r, c) for c in range(N)] for r in range(N)]

for r in range(N):
    for c in range(N):
        if (col_list[r] + row_list[c]) % 2 == 0:  
            for dr, dc in mv_list:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    if (col_list[nr] + row_list[nc]) % 2 == 0:
                        union(r, c, nr, nc)

for _ in range(Q):
    ra, ca, rb, cb = map(int, input().split())
    if find(ra-1, ca-1) == find(rb-1, cb-1):  # 최상위 부모 비교
        print("YES")
    else:
        print("NO")
