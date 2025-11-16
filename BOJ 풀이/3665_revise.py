# 위상정렬 문제
# IDEA : 작년도 순위로 방향 그래프를 만든다.
# 그리고, 순위가 뒤바뀐다 -> 그래프의 방향을 바꾼다.
# graph[x][y] = 1 ->  x보다 y의 순위가 더 높다.
# 순환선 발생시, 그 즉시 실패
# 동률이 발생시, 그 즉시 ?
# 두개를 구분해야 하므로, 순환선 판단을 위해 동률 발생시에도 강행해야 한다.

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    team = int(input())
    graph = [[0 for _ in range(team + 1)] for _ in range(team + 1)]
    
    rank_list = [0] + list(map(int, input().split()))
    
    for left in range(1, team):
        for right in range(left + 1, team + 1):
            left_team = rank_list[left]
            right_team = rank_list[right]
            graph[left_team][right_team] = 1
            
    change_cnt = int(input())
    for _ in range(change_cnt):
        cl, cr = map(int, input().split())
        graph[cl][cr] = 1 - graph[cl][cr]
        graph[cr][cl] = 1 - graph[cr][cl]
        
    next_set = [[] for _ in range(team + 1)]
    indegree = [0 for _ in range(team + 1)]
    for left in range(1, team + 1):
        for right in range(1, team + 1):
            if graph[left][right] == 1:
                next_set[left].append(right)
                indegree[right] += 1
    
    # 두 개의 플래그를 들고 위상정렬 시작
    no_common_rank_flag = True
    result_list = []
    
    q = deque()
    for i in range(1, team + 1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        # 동률이 두개 이상인 경우를 항상 체크해야 한다.
        # 왜냐면 동률이 발생하지 않았다면, 넣을 때 한개만 넣게 될 거라.
        if len(q) > 1:
            no_common_rank_flag = False
        cur_team = q.popleft()
        result_list.append(cur_team)
        next_team_list = next_set[cur_team]
        for nt in next_team_list:
            indegree[nt] -= 1
            if indegree[nt] == 0:
                q.append(nt)
    # 처음이든, 중간이든 cycle이 있을 경우에는 결과가 부족하게 되므로.
    if len(result_list) != team:
        print("IMPOSSIBLE")
    elif not no_common_rank_flag:
        print("?")
    else:
        for r in result_list:
            print(r, end = " ")
        print("")