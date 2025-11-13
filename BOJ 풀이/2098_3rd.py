import sys
input = sys.stdin.readline

INF = 10**15

def dfs(cur_v, visited, cur_dist):
    global ans

    # 가지치기 1: 상한
    if cur_dist >= ans:
        return

    # 가지치기 2: 현재 상태 dp 컷 (이미 더 싸게 왔다면 종료)
    if cur_dist >= dp[visited][cur_v]:
        return
    dp[visited][cur_v] = cur_dist

    # 모두 방문 → 0으로 귀환
    if visited == ALL:
        w_back = graph[cur_v][0]
        if w_back > 0:
            total = cur_dist + w_back
            if total < ans:
                ans = total
        return

    # 다음 도시 탐색 (이웃 리스트 없이)
    for next_v in range(N):
        w = graph[cur_v][next_v]
        if w == 0:
            continue
        bit = 1 << next_v
        if visited & bit:
            continue

        next_mask = visited | bit
        next_dist = cur_dist + w

        # 가지치기 3: 다음 상태 dp 컷 (그 상태로 더 싸게 온 적 있으면 가지치기)
        if next_dist >= dp[next_mask][next_v]:
            continue

        dfs(next_v, next_mask, next_dist)

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

N = len(graph)
ALL = (1 << N) - 1

# dp[mask][u] := mask 상태에서 u에 도달하는 최소 비용
dp = [[INF] * N for _ in range(1 << N)]

ans = INF
start_mask = 1 << 0
dfs(0, start_mask, 0)
print(ans if ans < INF else -1)