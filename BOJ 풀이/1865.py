# 벨만 포드 알고리즘을 araboza
# 한 노드에서 다른 노드 까지의 최단 거리를 알아내는 또 다른 알고리즘
# 이번엔 음의 가중치도 가능하다. 매 단계마다, 모든 간선을 확인하며 최단 거리를 구해 나가서.
# 음의 가중치가 들어가면 이걸 또 타서 줄일 수 있다. 문제는 음의 가중치 때문에 음의 사이클이 터지면 어떡함?
# 지금까지의 이웃까지의 거리보다, 현재 정점을 거치는게 유리하면..? 체크.

import sys
input = sys.stdin.readline
def bellman_ford(vertex, edge_list, dist):
    dist[1] = 0
    for i in range(vertex): 
        for j in range(len(edge_list)):
            cur_v, next_v, cur_cost = edge_list[j]
            if dist[next_v] > dist[cur_v] + cur_cost:
                dist[next_v] = dist[cur_v] + cur_cost
                # 만일 꼭지점 개수만큼 돌고 있다면..? 음의 사이클 발생.
                # why? 최단 경로는 최악의 경우 V-1개라고 가정한다.
                # 즉, 거리가 갱신되었는데 V번째 돌고 있다면 어딘가 음의 사이클 발생으로 볼 수 있다.!
                # 왜냐면, 양의 거리였다면 갔던데를 어디 뭐 다시 가서 사이클이 생길리가 없음 V-1 확정
                # 음일 사이클이 있으면 V-1 돌고도 갱신될 만한 여지가 있어서 또 갱신 되었다를 의미함.
                if i == vertex - 1:
                    return "YES"
    return "NO"
            
t_case = int(input())
for _ in range(t_case):
    vertex, road, hole = map(int, input().split())
    edge_list = []
    
    # 양방향 양의 거리
    for _ in range(road):
        start, end, time = map(int, input().split())
        edge_list.append([start, end, time])
        edge_list.append([end, start, time])
    # 단반향 음의 거리
    for _ in range(hole):
        start, end, time = map(int, input().split())
        edge_list.append([start, end, -time])
    
    # bellman-ford
    dist = [1e12] * (vertex + 1)
    print(bellman_ford(vertex, edge_list, dist))
        