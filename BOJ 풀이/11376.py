# 11376
# 한 사람당 최대 2개 까지 가능함
# 좌측에서 동일 조건을 2개로 늘려버리면 그만이다.

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

emp, work = map(int, input().split())
graph = [[]]
for _ in range(emp):
    cur_list = list(map(int, input().split()))
    # 예제를 보면 할 수 있는 일이 0개인 경우가 있어서, 이를 위한 고려
    # 어차피 0은 아예 무능력이라 매칭에서 고려할 필요도 없다.
    if len(cur_list) > 1:
        graph.append(cur_list[1:])
        graph.append(cur_list[1:])
        
ans = 0
matchR = [-1 for _ in range(work + 1)]

for cur_emp in range(1, len(graph)):
    visited = [False for _ in range(work + 1)]
    if find_pair(cur_emp):
        ans += 1
print(ans)