import sys
from collections import deque
input = sys.stdin.readline

def bipartite_check(start):
    gender_list[start] = 0
    global flag
    q = deque()
    q.append(start)
    
    while q:
        cur_v = q.popleft()
        nv_list = graph[cur_v]
        for nv in nv_list:
            if gender_list[nv] == -1:
                gender_list[nv] = 1 - gender_list[cur_v]
                q.append(nv)
            elif gender_list[nv] == gender_list[cur_v]:
                flag = False
                break

      
T = int(input())
for cur_cases in range(1, T+1):
    vertex, edge = map(int, input().split())
    graph = [[] for _ in range(vertex + 1)]
    for _ in range(edge):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)
    gender_list = [-1 for _ in range(vertex + 1)]
    
    flag = True
    for i in range(1, vertex + 1):
        if gender_list[i] == -1:
            bipartite_check(i)
    print('Scenario #%d:' %(cur_cases))
    if flag:
        print('No suspicious bugs found!')
    else:
        print('Suspicious bugs found!')
    print()