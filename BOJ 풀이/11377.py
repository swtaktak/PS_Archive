# 전원이 한 번에 두 개가 아니라, 한계치가 있다.
# 그러면 매칭 히스토리를 가지고, 쭉 이어가면 된다.
# 한 바퀴 더 돌자.

import sys
input = sys.stdin.readline

def find_pair(left):
    for right in graph[left]:
        if visited[right]:
            continue
        visited[right] = True
        
        if matchR[right] == -1 or find_pair(matchR[right]):
            matchR[right] = left
            return True
    return False

emp, work, double_work_limit = map(int, input().split())
graph = [[]]
for _ in range(emp):
    cur_list = list(map(int, input().split()))
    # 예제를 보면 할 수 있는 일이 0개인 경우가 있어서, 이를 위한 고려
    # 어차피 0은 아예 무능력이라 매칭에서 고려할 필요도 없다.
    if len(cur_list) > 1:
        graph.append(cur_list[1:])
        
ans = 0
matchR = [-1 for _ in range(work + 1)]

for cur_emp in range(1, len(graph)):
    visited = [False for _ in range(work + 1)]
    if find_pair(cur_emp):
        ans += 1
        
# 추가 부분 : double_cnt
double_cnt = 0
for cur_emp in range(1, len(graph)):
    visited = [False for _ in range(work + 1)]
    if find_pair(cur_emp):
        ans += 1
        double_cnt += 1
    if double_cnt == double_work_limit:
        break
    
print(ans)