import sys
import heapq
input = sys.stdin.readline
mv_list = [[-1, 0], [1, 0], [0, 1], [0, -1]]
INF = 1e9

def dijkstra(sx, sy):
    q = []
    heapq.heappush(q, (0, sx, sy)) # cost, x좌표, y좌표
    
    while q:
        cur_cost, cx, cy = heapq.heappop(q)
        if cur_cost > dist[cx][cy]:
            continue
        
        for nx, ny, next_cost in graph[cx][cy]:
            new_cost = next_cost + dist[cx][cy]
            if dist[nx][ny] > new_cost:
                dist[nx][ny] = new_cost
                heapq.heappush(q, (new_cost, nx, ny))
        if dist[rows-1][cols-1] == 0:
            break
cols, rows = map(int, input().split())
maze = []
for _ in range(rows):
    cur_row = [int(x) for x in list(str(input().rstrip()))]
    maze.append(cur_row)
graph = [[[] for _ in range(cols)] for _ in range(rows)]
dist = [[INF for _ in range(cols)] for _ in range(rows)]

# 양방향 그래프를 만들어보자.
for i in range(rows):
    for j in range(cols):
        for mv in mv_list:
            nx, ny = i + mv[0], j + mv[1]
            if 0 <= nx < rows and 0 <= ny < cols:
                graph[i][j].append((nx, ny, maze[nx][ny]))
dist[0][0] = 0
# 다익스트라를 하자.

dijkstra(0, 0)
print(dist[-1][-1])