import sys
import heapq
input = sys.stdin.readline

# 높이 매핑
def h(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    return ord(c) - ord('a') + 26


# 다익스트라
def dijkstra(start, graph, N):
    INF = 10**15
    dist = [INF] * N
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        cost, u = heapq.heappop(pq)
        if cost > dist[u]:
            continue
        for v, w in graph[u]:
            nc = cost + w
            if nc < dist[v]:
                dist[v] = nc
                heapq.heappush(pq, (nc, v))
    return dist


# 입력
R, C, T, D = map(int, input().split())
mountain = [list(map(h, input().rstrip())) for _ in range(R)]

N = R * C

# 그래프 구성
graph = [[] for _ in range(N)]
idx = lambda r, c: r*C + c

for r in range(R):
    for c in range(C):
        u = idx(r, c)
        hu = mountain[r][c]

        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                v = idx(nr, nc)
                hv = mountain[nr][nc]

                # 고도 차 조건
                if abs(hu - hv) <= T:
                    # u → v
                    if hv <= hu:
                        w = 1
                    else:
                        w = (hv - hu)**2
                    graph[u].append((v, w))

                    # v → u
                    if hu <= hv:
                        w2 = 1
                    else:
                        w2 = (hu - hv)**2
                    graph[v].append((u, w2))


# (0,0)에서 출발
start = 0
go = dijkstra(start, graph, N)

answer = mountain[0][0]

# 모든 노드에 대해 왕복 가능성 체크
for v in range(N):
    if go[v] > D:
        continue  # 도달 불가 or 왕복 불가 확정

    # v에서 출발해서 0까지 다익스트라
    back = dijkstra(v, graph, N)

    if go[v] + back[0] <= D:
        r = v // C
        c = v % C
        answer = max(answer, mountain[r][c])

print(answer)
