# 아예 그래프를 만들어서 indegree가 0인 애를 찾아줘야 한다.
import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]] # D U R L

N = int(input())
forest = []
for _ in range(N):
    forest.append(list(map(int, input().split())))
indegree_cnt = [[0 for _ in range(N)] for _ in range(N)]
graph = [[[] for _ in range(N)] for _ in range(N)]
max_cnt = 0

# 방문 여부는 대소 비교의 특성상 담지 않아도 되려나?
def dfs(x, y, cur_level):
    global max_cnt
    if max_cnt < cur_level:
        max_cnt = cur_level
    for nx, ny in graph[x][y]:
        dfs(nx, ny, cur_level + 1)

# step 1.  그래프와 차수를 정보를 가져와야 한다.
for i in range(N):
    for j in range(N):
        for mv in mv_list:
            nx, ny = i + mv[0], j + mv[1]
            if 0 <= nx < N and 0 <= ny < N:
                # 주의! 양방향 비교가 아닌 한 쪽 방향만 비교해야 한다.
                if forest[i][j] > forest[nx][ny]:
                    indegree_cnt[i][j] += 1
                    graph[nx][ny].append((i, j))

# step 2. indegree 0인 지점에서 출발한다.
start_pos = []
for i in range(N):
    for j in range(N):
        if indegree_cnt[i][j] == 0:
            dfs(i, j, 1)
print(max_cnt)