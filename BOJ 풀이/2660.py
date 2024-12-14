# 플로이드 와샬로, 해야 한다.
# 전체 거리 중 최대를 뽑아내야 하므로.
N = int(input())
INF = 1e9
dist = [[INF for _ in range(N+1)] for _ in range(N+1)]

while True:
    a, b = map(int, input().split())
    
    if a == -1 and b == -1:
        break
    else: 
        dist[a][b] = 1
        dist[b][a] = 1

for i in range(1, N+1):
    dist[i][i] = 0
    
for mid in range(1, N+1):
    for s in range(1, N+1):
        for e in range(1, N+1):
            dist[s][e] = min(dist[s][e], dist[s][mid] + dist[mid][e])
cand_level = [INF] * (N+1)
for i in range(1, N+1):
    cur_dist = dist[i][1:]
    cand_level[i] = max(cur_dist)

cand_score = min(cand_level)
cand_list = []
cands = 0
for i in range(1, N+1):
    if cand_level[i] == cand_score:
        cands += 1
        cand_list.append(i)

print("%d %d" %(cand_score, cands))
for c in cand_list:
    print(c, end = " ")