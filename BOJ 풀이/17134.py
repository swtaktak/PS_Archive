# 14433
# 문제 겁나 웃기네 ㅋㅋㅋ
# 팀원 - 트롤픽이 더 많아야 승급

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_pair(left, matchR, graph):
    for right in graph[left]:
        if visited[right]:
            continue
        visited[right] = True
    
        if matchR[right] == -1 or find_pair(matchR[right], matchR, graph):
            matchR[right] = left
            return True
    return False

mem, troll, t1, t2 = map(int, input().split())

# 이분매칭 그래프 생성
graph_t1 = [[] for _ in range(mem + 1)]
graph_t2 = [[] for _ in range(mem + 1)]

for _ in range(t1):
    player, pick = map(int, input().split())
    graph_t1[player].append(pick)
for _ in range(t2):
    player, pick = map(int, input().split())
    graph_t2[player].append(pick)
    

t1_pick = 0
t2_pick = 0
matchR1 = [-1 for _ in range(troll + 1)]
matchR2 = [-1 for _ in range(troll + 1)]

# t1 매칭
for left in range(1, mem + 1):
    visited = [False for _ in range(troll + 1)]
    if find_pair(left, matchR1, graph_t1):
        t1_pick += 1
# t2 매칭
for left in range(1, mem + 1):
    visited = [False for _ in range(troll + 1)]
    if find_pair(left, matchR2, graph_t2):
        t2_pick += 1
        
if t1_pick < t2_pick:
    print('네 다음 힐딱이')
else:
    print('그만 알아보자')