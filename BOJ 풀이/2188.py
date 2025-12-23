# 이분매칭의 개념을 배우는 문제

import sys
input = sys.stdin.readline

def find_pair(left):
    for right in graph[left]:
        # 이번 탐색에서 시도한 right는 다시 시도하지 않게.
        if visited[right]:
            continue
        visited[right] = True # 새로운 짝을 찾았다.
    
        # 현재 right가 짝이 없으면 left랑 준다.
        # 현재 right가 짝이 있다면, 기존 left는 새로운 짝을 찾는다.
        if matchR[right] == -1 or find_pair(matchR[right]):
            # right는 짝이 없거나 right의 옛 짝이 새 짝을 찾았다.
            matchR[right] = left # 현재 right의 짝은 left 성공
            return True
    
    # 모든 경우가 다 실패해서
    # 현재 left는 짝을 찾을 수 없다.
    return False
cow, farm = list(map(int, input().split()))

graph = [[]]

for i in range(1, cow + 1):
    cur_list = list(map(int, input().split()))
    graph.append(cur_list[1:])
    
ans = 0
matchR = [-1 for _ in range(farm + 1)]
# 이분 매칭을 실시한다.
for left in range(1, cow + 1):
    visited = [False for _ in range(farm + 1)]
    if find_pair(left):
        ans += 1
print(ans)

# 시간복잡도?
# 최악 케이스는 모든 경우가 연결되며 모든 꼭지점 확인
# LEFT ^ 2 * RIGHT