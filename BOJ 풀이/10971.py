import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(level):
    global min_cost
    if level == N:
        cur_cost = 0
        for i in range(1, N):
            cur_cost += cost_list[trv[i-1]][trv[i]]
        cur_cost += cost_list[trv[-1]][trv[0]]
        min_cost = min(cur_cost, min_cost)
        return

    for i in range(0, N):
        if not visited[i]:
            visited[i] = True
            trv.append(i)
            dfs(level + 1)
            visited[i] = False
            trv.pop()

N = int(input())
cost_list = []
for _ in range(N):
    cur_row = list(map(int, input().split()))
    for i in range(N):
        if cur_row[i] == 0:
            cur_row[i] = 999999999
    cost_list.append(cur_row)

min_cost = 999999999
visited = [False] * (N)
trv = []
dfs(0)
print(min_cost)