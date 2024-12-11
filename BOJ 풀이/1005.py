import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    vertex, edge = map(int, input().split())
    # 건물의 순서를 고려하기 위해 위상정렬을 사용한다.
    indegree_list = [0] * (vertex + 1)
    cur_time = [0] * (vertex + 1)
    v_time = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(vertex + 1)]

    for _ in range(edge):
        start, end = map(int, input().split())
        indegree_list[end] += 1
        graph[start].append(end)
    
    goal = int(input())
    
    q = deque()
    for i in range(1, vertex + 1):
        if indegree_list[i] == 0:
            q.append(i)
            # 바로 지을 수 있는 건물은 초기 값을 선정한다.
            cur_time[i] = v_time[i]
    while q:
        # 이제 이 다음거를 건설하러 간다.
        cur_v = q.popleft()
        nv_list = graph[cur_v]
        for nv in nv_list:
            indegree_list[nv] -= 1
            # 선행 작업이 완료되어 건축이 가능하다.
            cur_time[nv] = max(cur_time[nv], cur_time[cur_v] + v_time[nv]) 
            if indegree_list[nv] == 0:
                q.append(nv)
    print(cur_time[goal])
        