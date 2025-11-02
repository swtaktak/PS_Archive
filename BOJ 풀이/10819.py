import sys
input = sys.stdin.readline

def dfs(level):
    global ans
    if level == N:
        cur_diff = 0
        for i in range(1, N):
            cur_diff += abs(pick_list[i] - pick_list[i-1])
        ans = max(cur_diff, ans)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            pick_list.append(num_list[i])
            dfs(level + 1)
            visited[i] = False
            pick_list.pop()
            
N = int(input())
num_list = list(map(int, input().split()))
visited = [False for _ in range(N)]
pick_list = []
ans = -1

dfs(0)
print(ans)