# 1949
# Tree- DP 연습 문제

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
num_list = [-1] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    left, right = map(int, input().split())
    graph[left].append(right)
    graph[right].append(left)

dp = [[0, 0] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

def dfs(cur_v):
    visited[cur_v] = True
    dp[cur_v][1] = num_list[cur_v]
    
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            dfs(next_v)
            dp[cur_v][1] += dp[next_v][0]
            dp[cur_v][0] += max(dp[next_v][0], dp[next_v][1])
            # 비우수가 우수에 인접 못 할리가 없어짐
            # 최댓값을 구할 때, 점수가 strictly 양 득점이기 때문이다.
dfs(1)
print(max(dp[1][0], dp[1][1]))