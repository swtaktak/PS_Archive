# dfs, bfs로만 풀면 시간 초과나 메모리 초과가 발생한다.
# DP + DFS를 하는 방법을 배워보자.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def dfs(cx, cy):
    # 순환은 발생하지 않으나, 방문 반복 체크를 막기 위함
    if dp[cx][cy] != -1:
        return dp[cx][cy]

    dp[cx][cy] = 1
    for mv in mv_list:
        nx = cx + mv[0]
        ny = cy + mv[1]
        if 0 <= nx < N and 0 <= ny < N:
            if forest[nx][ny] > forest[cx][cy]:
                # 한칸 더 갈 수 있으면, 그 깊이를 +1 +1 ..해서 저장한다.
                # 이거 자체가 경로를 기억하는 효과가 있어 돌아오는 거마다 -1씩 까인다.
                dp[cx][cy] = max(dp[cx][cy], dfs(nx, ny) + 1)
    return dp[cx][cy]


N = int(input())
forest = []
for _ in range(N):
    forest.append(list(map(int, input().split())))

dp = [[-1 for _ in range(N)] for _ in range(N)]
answer = 0

for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))
print(answer)