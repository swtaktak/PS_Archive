# 아예 그래프를 만들어서 indegree가 0인 애를 찾아줘야 한다.
import sys
from collections import deque
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]] # D U R L

N = int(input())
forest = []
for _ in range(N):
    forest.append(list(map(int, input().split())))
indegree_cnt = [[0 for _ in range(N)] for _ in range(N)]
graph = [[[] for _ in range(N)] for _ in range(N)]
max_cnt = 0

def bfs(x, y):
    global max_cnt
    queue = deque()
    queue.append([x, y, 1])
    
    while queue:
        cx, cy, cur_cnt = queue.popleft()
        if cur_cnt > max_cnt:
            max_cnt = cur_cnt
        next_list = graph[cx][cy]
        for nx, ny in next_list:
            queue.append([nx, ny, cur_cnt + 1])

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
            bfs(i, j)
print(max_cnt)