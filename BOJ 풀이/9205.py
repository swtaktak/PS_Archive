import sys
from collections import deque
input = sys.stdin.readline

def l1_dist(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    return dx + dy

# 어렵게 생각하지 말자. 거리가 1000 이하로 계속 이동이 가능한가?
# 딱뎀 1000까지는 ㅇㅋㅋ
T = int(input())
for _ in range(T):
    num_conv = int(input())
    hx, hy = map(int, input().split())
    points = []
    visited = {}
    for _ in range(num_conv):
        cx, cy = map(int, input().split())
        points.append([cx, cy])
        visited[(cx, cy)] = False
    gx, gy = map(int, input().split())
    points.append([gx, gy])
    visited[(gx, gy)] = False
    happy_flag = False
    q = deque()
    q.append([hx, hy])
    
    while q:
        cx, cy = q.popleft()
        for nx, ny in points:
            if not visited[(nx, ny)] and l1_dist(cx, cy, nx, ny) <= 1000:
                if nx == gx and ny == gy:
                    happy_flag = True
                    break
                else:
                    visited[(nx, ny)] = True
                    q.append([nx, ny])
    if happy_flag:
        print('happy')
    else:
        print('sad')
    # 갈 수 있는데 빙 돌아 가는건 의미가 없다. 술은 어차피 무한리필된다.