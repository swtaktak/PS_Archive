import sys
input = sys.stdin.readline

def dfs(level, cur_list, visited):
    global ans_list
    if ans_list != []:
        return
    elif level == N:
        sum = 0
        for i in range(N):
            sum += (cur_list[i] * weight[i])
        if sum == target:
            ans_list = cur_list.copy()
        return
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            cur_list.append(i)
            dfs(level + 1, cur_list, visited)
            cur_list.pop()
            visited[i] = False

# step 1 / 파스칼 삼각형으로 가중치 만들기
N, target = map(int, input().split())
pas = [[1 for _ in range(N)] for _ in range(N)]
for i in range(1, N):
    for j in range(1, i):
            pas[i][j] = pas[i-1][j-1] + pas[i-1][j]
weight = pas[-1]
# step 2 / dfs 돌리기
ans_list = []
visited = [False for _ in range(N+1)]
dfs(0, [], visited)
# 정답 행렬 출력하기.

for a in ans_list:
    print(a, end = ' ')