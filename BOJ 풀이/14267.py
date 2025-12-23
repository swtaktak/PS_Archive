import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, praise = map(int, input().split())
boss_list = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]

# graph 먼저 만들기
for junior in range(2, N + 1):
    boss = boss_list[junior]
    graph[boss].append(junior)
    graph[junior].append(boss)
    
p_list = [0 for _ in range(N + 1)]
for _ in range(praise):
    emp, point = map(int, input().split())
    p_list[emp] += point

dp = [0 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

def dfs(cur_v):
    visited[cur_v] = True
    dp[cur_v] += p_list[cur_v]
    
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            dp[next_v] += dp[cur_v]
            dfs(next_v)

dfs(1)
for i in range(1, N + 1):
    print(dp[i], end = " ")
