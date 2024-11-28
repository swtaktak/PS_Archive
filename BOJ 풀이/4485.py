import sys
import heapq
input = sys.stdin.readline
mv_list = [[1, 0], [-1, 0], [0, 1], [0, -1]]
def dijkstra(sx, sy):
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (0, sx, sy)) # 비용, row, col
    
    while q:
        cur_cost, cx, cy = heapq.heappop(q)
        if cost_list[cx][cy] < cur_cost:
            continue
        
        for nx, ny, next_cost in graph[cx][cy]:
            new_cost = next_cost + cur_cost
            if new_cost < cost_list[nx][ny]:
                cost_list[nx][ny] = new_cost
                heapq.heappush(q, (new_cost, nx, ny)) 

cur_case = 1
INF = 1e9
while True:
    N = int(input())
    if N != 0:
        cave = []
        for _ in range(N):
            cave.append(list(map(int, input().split())))
        # 첫 칸은 무조건 뜯긴다.
        first = cave[0][0]
        graph = [[[] for _ in range(N)] for _ in range(N)]
        cost_list = [[INF for _ in range(N)] for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                for mv in mv_list:
                    nx, ny = i + mv[0], j + mv[1]
                    if 0 <= nx < N and 0 <= ny < N:
                        # 다음지점, 다음 지점에서 뜯겨버릴 루피.
                        graph[i][j].append([nx, ny, cave[nx][ny]])
        dijkstra(0, 0)         
        answer = cost_list[-1][-1] + first
        print("Problem %d: %d" %(cur_case, answer))
        cur_case += 1
    else:
        break