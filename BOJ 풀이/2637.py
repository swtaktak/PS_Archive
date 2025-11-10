import sys
from collections import deque
input = sys.stdin.readline

# 위상정렬 + dp 형태?
# 뭐가 기본인지 모르는게 문제.

parts = int(input())
rels = int(input())
next_list = [[] for _ in range(parts + 1)]
indegree_list = [0] * (parts + 1)

# 위상정렬을 위해
for _ in range(rels):
    end, start, cost = map(int, input().split())
    next_list[start].append((end, cost))
    indegree_list[end] += 1
    
q = deque()
basic_parts = []
# 출발점은 indegree 0이므로. 이것이 기본부품이기도 하다. 중간 단계가 없으므로.
for i in range(1, parts + 1):
    if indegree_list[i] == 0:
        q.append(i)
        basic_parts.append(i)
        
dp_table = [[0 for _ in range(parts + 1)] for _ in range(parts + 1)]

while q:
    cur_item = q.popleft()
    for next_item, req_cnt in next_list[cur_item]:
        # 기본 아이템일 경우
        if cur_item in basic_parts:
            dp_table[next_item][cur_item] += req_cnt
        # 중간 산물일 경우.
        else:
            for i in range(1, parts + 1):
                dp_table[next_item][i] += (dp_table[cur_item][i] * req_cnt)
        indegree_list[next_item] -= 1
        if indegree_list[next_item] == 0:
            q.append(next_item)

for b in basic_parts:
    print("%d %d"%(b, dp_table[-1][b]), end = "\n")