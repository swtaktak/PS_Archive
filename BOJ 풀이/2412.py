import sys
from collections import deque
input = sys.stdin.readline

holes, target_h = map(int, input().split())
hole_list = set()
for _ in range(holes):
    cx, cy = map(int, input().split())
    hole_list.add((cx, cy))
    
q = deque()
q.append((0, 0, 0)) # x, y, grabs

flag = False
while q:
    cx, cy, cnt = q.popleft()
    if cy == target_h:
        answer = cnt
        flag = True
        break
    
    for i in range(-2, 3):
        for j in range(-2, 3):
            nx = cx + i
            ny = cy + j
            if (nx, ny) in hole_list:
                q.append((nx, ny, cnt + 1))
                hole_list.remove((nx, ny))
if not flag:
    print(-1)
else:
    print(answer)