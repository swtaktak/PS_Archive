import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],]


que = deque()
M, N, O, P, Q, R, S, T, U, V, W = map(int, input().split())
tomato = [[[[[[[[[[list(map(int, input().split())) for _ in range(N)]for _ in range(O)]for _ in range(P)]for _ in range(Q)]for _ in range(R)]for _ in range(S)]for _ in range(T)]for _ in range(U)]for _ in range(V)]for _ in range(W)]
left_space = 0
for m in range(M):
    for n in range(N):
        for o in range(O):
            for p in range(P):
                for q in range(Q):
                    for r in range(R):
                        for s in range(S):
                            for t in range(T):
                                for u in range(U):
                                    for v in range(V):
                                        for w in range(W):
                                            if tomato[w][v][u][t][s][r][q][p][o][n][m] == 1:
                                                que.append((0, w, v, u, t, s, r, q, p, o, n, m))
                                            elif tomato[w][v][u][t][s][r][q][p][o][n][m] == 0:
                                                left_space += 1                                             
# tomato에다가 바로 visited 생각
while que:
    cur_day, cw, cv, cu, ct, cs, cr, cq, cp, co, cn, cm = que.popleft()
    for mv in mv_list:
        nw = cw + mv[0]
        nv = cv + mv[1]
        nu = cu + mv[2]
        nt = ct + mv[3]
        ns = cs + mv[4]
        nr = cr + mv[5]
        nq = cq + mv[6]
        np = cp + mv[7]
        no = co + mv[8]
        nn = cn + mv[9]
        nm = cm + mv[10]
        
        if 0 <= nw < W and 0 <= nv < V and 0 <= nu < U and 0 <= nt < T and 0 <= ns < S and 0 <= nr < R and 0 <= nq < Q and 0 <= np < P and 0 <= no < O and 0 <= nn < N and 0 <= nm < M:
            if tomato[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] == 0:
                tomato[nw][nv][nu][nt][ns][nr][nq][np][no][nn][nm] = 1
                left_space -= 1
                que.append((cur_day + 1, nw, nv, nu, nt, ns, nr, nq, np, no, nn, nm))
if left_space > 0:
    print(-1)
else:
    print(cur_day)