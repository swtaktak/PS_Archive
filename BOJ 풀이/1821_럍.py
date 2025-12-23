import sys
input = sys.stdin.readline

class Found(Exception):
    pass

def dfs(level, cur_list, visited):
    if level == N:
        total = sum(cur_list[i] * weight[i] for i in range(N))
        if total == target:
            print(*cur_list)
            raise Found   # ★ 정답 찾자마자 전체 종료
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            cur_list.append(i)
            dfs(level + 1, cur_list, visited)
            cur_list.pop()
            visited[i] = False


# 1) 파스칼 가중치 계산
N, target = map(int, input().split())
pas = [[1] * N for _ in range(N)]
for i in range(1, N):
    for j in range(1, i):
        pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
weight = pas[-1]

# 2) DFS + 강제 종료
visited = [False] * (N + 1)

try:
    dfs(0, [], visited)
except Found:
    pass
