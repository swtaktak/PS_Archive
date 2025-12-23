# DP + DFS의 가장 기본적인 문제

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur_v):
    global dp
    dp[cur_v] = 1
    for nv in graph[cur_v]:
        if not visited[nv]:
            visited[nv] = True
            dp[cur_v] += dfs(nv)
    return dp[cur_v]


vertex, root, query = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]

for _ in range(vertex - 1):
    left, right = map(int, input().split())
    graph[left].append(right)
    graph[right].append(left)
    
visited = [False for _ in range(vertex + 1)]
dp = [0 for _ in range(vertex + 1)]

visited[root] = True
dfs(root)

for _ in range(query):
    print(dp[int(input())])