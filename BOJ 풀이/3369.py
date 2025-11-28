import sys
input = sys.stdin.readline

def dist_sq(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

ans_list = ['X']
# graph[i][j]는 도시 j가 도시 i에게 주는 영향력임
N = int(input())
city_dict = {}

for i in range(1, N+1):
    x, y, sol = map(int, input().split())
    city_dict[i] = [x, y, sol]
graph = [[-1 for _ in range(N+1)] for _ in range(N+1)]

for def_city in range(1, N+1):
    for att_city in range(1, N+1):
        if def_city != att_city:
            ax, ay, a_sol = city_dict[att_city]
            dx, dy, d_sol = city_dict[def_city]
            graph[def_city][att_city] = a_sol / dist_sq(ax, ay, dx, dy)
            
# 각 도시별로 판별임
# 만일 받는 영향력보다 자신의 군사력이 더 클 경우 K
# 만일 받는 영향이 더 큰게 있는데 그게 동률이 2개 이상인 경우 D
# 다른 도시 혼자만 최대로 영향 더 크게 주면 그 도시 번호 출력

for cur_city in range(1, N+1):
    cur_sol = city_dict[cur_city][2]
    max_inf = -1
    for att_city in range(1, N+1):
        if cur_city != att_city:
            if graph[cur_city][att_city] > cur_sol:
                max_inf = max(max_inf, graph[cur_city][att_city])
    if max_inf == -1:
        ans_list.append('K')
    else:
        max_cnt = 0
        for att_city in range(1, N+1):
            if att_city != cur_city and graph[cur_city][att_city] == max_inf:
                max_cnt += 1
        if max_cnt == 1:
            ans_list.append(str(graph[cur_city].index(max_inf)))
        else:
            ans_list.append('D')


for i in range(1, N + 1):
    # 민주도시거나 자립수도거나 왕국수도도 아닌 경우
    # 최종적으로 복속 당할 곳을 찾는다.
    if ans_list[i] not in ['K', 'D']:
        while ans_list[int(ans_list[i])] != 'K':
            ans_list[i] = ans_list[int(ans_list[i])]
    print(ans_list[i])