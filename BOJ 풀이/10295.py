import sys
import heapq
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1],
           [1, 1], [1, -1], [-1, 1], [-1, -1]]
input = sys.stdin.readline

INF = 1e12

def dijkstra(start):
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_cost > dist[cur_v]:
            continue
        for next_v, next_cost in graph[cur_v]:
            new_cost = next_cost + cur_cost
            if new_cost < dist[next_v]:
                dist[next_v] = new_cost
                heapq.heappush(pq, (new_cost, next_v))

T = int(input())
# -1이 장애물, 위험구역
for _ in range(T):
    max_val = -1
    goal_r = -1
    goal_c = -1
    rows, cols = map(int, input().split())
    maps = [[] for _ in range(rows)]
    for r in range(rows):
        cur_row = str(input().rstrip())
        for c in range(cols):
            if cur_row[c] != '#':
                maps[r].append(int(cur_row[c]))
                # 도착지점을 한 번에 찾는다.
                if int(cur_row[c]) > max_val:
                    max_val = int(cur_row[c])
                    goal_r = r
                    goal_c = c
            else:
                maps[r].append(-1)
    # 사전 읽는 순서대로 그래프를 만든다.
    graph = [[] for _ in range(rows * cols)]
    start_r, start_c = map(int, input().split())
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] != -1:
                for mv in mv_list:
                    nr = r + mv[0]
                    nc = c + mv[1]
                    if 0 <= nr < rows and 0 <= nc < cols and maps[nr][nc] != -1:
                        cur_coord = r * cols + c
                        next_coord = nr * cols + nc
                        if maps[r][c] == maps[nr][nc]:
                            graph[cur_coord].append((next_coord, 1))
                        else:
                            dist = (abs(maps[r][c] - maps[nr][nc]) + 1) ** 2
                            graph[cur_coord].append((next_coord, dist))
    # 그래프를 만들었다. 시작점부터 도착점까지를 다익스트라로 구하자.
    dist = [INF for _ in range(rows * cols)]
    start = start_r * cols + start_c
    goal = goal_r * cols + goal_c
    dijkstra(start)
    
    if dist[goal] == INF:
        print('NO')
    else:
        print(dist[goal])