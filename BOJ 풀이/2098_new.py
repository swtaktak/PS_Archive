import sys
input = sys.stdin.readline
INF = 10**15

def dfs(cur_v, visited):
    # 모두 방문: 시작(0)으로 귀환
    # 현재 방식에서는 이게 마지막 단계이므로 마지막을 합쳐준다.
    if visited == ALL:
        return graph[cur_v][0] if graph[cur_v][0] > 0 else INF

    # 메모이제이션
    if dp[visited][cur_v] != -1:
        return dp[visited][cur_v]

    best = INF
    for next_v in range(N):
        if (visited & (1 << next_v)) != 0:  # 이미 방문
            continue
        w = graph[cur_v][next_v]
        if w == 0:                           # 간선 없음
            continue
        cand = w + dfs(next_v, visited | (1 << next_v))
        if cand < best:
            best = cand
    # 현재 지점의 최적을 계속 더해준다.
    dp[visited][cur_v] = best
    return best

N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]

ALL = (1 << N) - 1
# dp[mask][u] := mask 상태에서 u에 있을 때 남은 최소 비용
dp = [[-1] * N for _ in range(1 << N)]

start_mask = 1 << 0
ans = dfs(0, start_mask)
print(ans if ans < INF else -1)
