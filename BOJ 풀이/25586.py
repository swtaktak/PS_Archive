# 25586
# IDEA > 넘어간 애는 걍 넣어 버리면 되지 않나?
# 아무튼 서열만 유지되면 되서 이것은 위상정렬이다.
import sys
from collections import deque
input = sys.stdin.readline

total_box, sub_box, add_cut = map(int, input().split())
graph = [[] for _ in range(total_box + 1)]
indegree = [0 for _ in range(total_box + 1)]
for i in range(1, total_box + 1):
    cur_list = list(map(int, input().split()))
    if cur_list[0] > 0:
        for c in cur_list[1:]:
            graph[i].append(c)
            indegree[c] += 1

ans = []
q = deque()
for i in range(1, total_box + 1):
    if indegree[i] == 0:
        start_v = i
        break
q.append(start_v)
while q:
    cur_v = q.popleft() 

    ans.append(cur_v)
    for nv in graph[cur_v]:
        indegree[nv] -= 1
        if indegree[nv] == 0:
            q.append(nv)

result = [[] for _ in range(total_box + 1)]
for i in range(0, len(ans)-1):
    left, right = ans[i], ans[i + 1]
    result[left].append(1)
    result[left].append(right)
result[ans[-1]].append(0)         


# 정답 출력 부분
print(1) # 가능
print(0) # 추가하는 상자 없음
for i in range(1, total_box + 1):
    cur_line = result[i]
    for c in cur_line:
        print(c, end = " ")
    print()
    