# 재귀나 그리디는 비효율적, 
# bfs 풀이는 메모리 초과를 당하고, dfs는 너무 느리다.

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
scv_list = list(map(int, input().split()))
while len(scv_list) < 3:
    scv_list.append(0)

q = deque()
q.append([scv_list[0], scv_list[1], scv_list[2], 0])

while q:
    cx, cy, cz, cnt = q.popleft()
    if cx <= 0 and cy <= 0 and cz <= 0:
        print(cnt)
        break
    else:
        q.append([cx-9, cy-3, cz-1, cnt + 1])
        q.append([cx-9, cy-1, cz-3, cnt + 1])
        q.append([cx-3, cy-9, cz-1, cnt + 1])
        q.append([cx-3, cy-1, cz-9, cnt + 1])
        q.append([cx-1, cy-3, cz-9, cnt + 1])
        q.append([cx-1, cy-9, cz-3, cnt + 1])