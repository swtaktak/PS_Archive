import sys
input = sys.stdin.readline

INF = 10**15
def dfs(cur_v, visited, cur_dist):
    global ans
    # 모든 도시 방문 → 0번으로 귀환
    if visited == (1 << N) - 1:
        if graph[cur_v][0] > 0:
            ans = min(ans, cur_dist + graph[cur_v][0])
        return

    for next_v in nonzero_list[cur_v]:
        if visited & (1 << next_v) == 0:
            next_mask = visited | (1 << next_v)
            next_dist = cur_dist + graph[cur_v][next_v]
            # 이미 더 좋은 상태로 온 적이 있다면, dfs 돌면 안됨.
            if next_dist >= dp[next_mask][next_v] and dp[next_mask][next_v] != -1:
                continue
            elif next_dist < ans:
                dp[next_mask][next_v] = next_dist
                dfs(next_v, next_mask, next_dist)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
nonzero_list = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            nonzero_list[i].append(j)

ans = INF
dp = [[-1 for _ in range(N)] for _ in range(1 << N)]

start_mask = 1 << 0   # 0번 도시 방문으로 시작
dp[1][0] = 0
dfs(0, start_mask, 0)
print(ans)