# 유니온 파인드 튜토리얼 문제
# Find : 재귀적으로 부모를 찾는다
# Union : 서로 다른 부모를 가진 노드를 합치는 행동. / 연결관계가 확실해짐

# 진실의 노드를 0으로 한다. 진실을 아는자, 0이라는 부모로 묶는다.

import sys
input = sys.stdin.readline

person, party = map(int, input().split())

truth_list = list(map(int, input().split()))
# 진실의 명단과, 진실을 분리한다.
if len(truth_list) == 0:
    truth_num = 0
    truth_list = []
else:
    truth_num = truth_list[0]
    truth_list = truth_list[1:]
    
parent_dict = {}
for i in range(1, person+1):
    parent_dict[i] = i    
# step 1 : 집합 분리 / 서로 한 번 이상 만난 사람 기준으로.
# 단, 부모는 가장 번호가 적은 것으로 통일한다. -> 최상 루트에 통일되어버림.
# 그 리 고, 이전에 그것이 부모였던 애들을 모두 또 부모를 변경해야 한다.
party_list = []
for _ in range(party):
    cur_party_list = list(map(int, input().split()))
    if cur_party_list[0] == 1:
        party_list.append([cur_party_list[1]])
    else:
        cur_party_list = cur_party_list[1:]
        party_list.append(cur_party_list)
        parent_num = [parent_dict[x] for x in cur_party_list]
        cur_parent = min(parent_num)
        # union 과정, 부모를 갱신해서 합쳐줘야 한다.
        for i in range(1, person + 1):
            if parent_dict[i] in parent_num:
                parent_dict[i] = cur_parent
                
# step 2 : 진실을 아는 사람의 부모와 같은 사람을 
for cur_truth in truth_list:
    # 진실을 아는 사람의 부모는?
    truth_parent = parent_dict[cur_truth]
    for i in range(1, person + 1):
        if parent_dict[i] == truth_parent:
            parent_dict[i] = 0

# step 3 : 재순회를 한다. 이미 그룹이 묶여 있으므로 원소 하나만 체크
answer = 0
for p in party_list:
    if parent_dict[p[0]] > 0:
        answer += 1
print(answer)