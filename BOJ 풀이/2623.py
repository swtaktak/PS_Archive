# 위상 정렬 튜토리얼 문제

import sys
from collections import deque
input = sys.stdin.readline

INF = 1e9
teams, seqs = map(int, input().split())
next_list = [[] for _ in range(teams + 1)]
indegree_list = [0] * (teams + 1)
indegree_list[0] = INF

for _ in range(seqs):
    cur_list = list(map(int, input().split()))
    if cur_list[0] == 1:
        pass
    elif cur_list[0] >= 2:
        for i in range(1, cur_list[0]):
            next_list[cur_list[i]].append(cur_list[i+1])
            indegree_list[cur_list[i+1]] += 1

answer_list = []
# 위상 정렬
queue = deque()
for i in range(1, teams + 1):
    if indegree_list[i] == 0:
        queue.append(i)
while queue:
    cur_team = queue.popleft()
    answer_list.append(cur_team)
    
    cur_next_team_list = next_list[cur_team]
    for next_team in cur_next_team_list:
        indegree_list[next_team] -= 1
        if indegree_list[next_team] == 0:
            queue.append(next_team)
if len(answer_list) == teams:
    for a in answer_list:
        print(a)
else:
    print(0)