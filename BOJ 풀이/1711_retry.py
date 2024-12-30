# 1711 직각삼각형 재시도
import sys
input = sys.stdin.readline

def is_right(a, b, c):
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    cx, cy = c[0], c[1]
    
    ab = (bx - ax) ** 2 + (by - ay) ** 2
    ac = (cx - ax) ** 2 + (cy - ay) ** 2
    bc = (cx - bx) ** 2 + (cy - by) ** 2
    
    if ab + ac == bc or ab + bc == ac or ac + bc == ab:
        return True
    else:
        return False

def dfs(level, cur_pos):
    global answer
    if level == 3:
        a, b, c = pick_list[0], pick_list[1], pick_list[2]
        if is_right(a, b, c):
            answer += 1
        return
    
    for i in range(cur_pos, N):
        if not visited[i]:
            visited[i] = True
            pick_list.append(coords[i])
            dfs(level + 1, i + 1)
            visited[i] = False
            pick_list.pop()
    
N = int(input())
visited = [False] * (N)
pick_list = []
coords = []
for _ in range(N):
    cx, cy = map(int, input().split())
    coords.append((cx, cy))
answer = 0

dfs(0, 0)
print(answer)