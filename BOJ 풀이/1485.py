import sys
input = sys.stdin.readline

def dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

T = int(input())
for _ in range(T):
    coords = []
    for _ in range(4):
        x, y = map(int, input().split())
        coords.append((x, y))
    coords.sort()
    # 반시계/시계 방향으로 정렬
    coords[2], coords[3] = coords[3], coords[2]
    
    judge = True
    for i in range(4):
        if i == 0:
            cur_dist = dist(coords[0][0], coords[0][1], coords[1][0], coords[1][1])
        else:
            new_dist = dist(coords[i%4][0], coords[i%4][1], coords[(i+1)%4][0], coords[(i+1)%4][1])
            if cur_dist != new_dist:
                judge = False
    if judge:
        diag1 = dist(coords[0][0], coords[0][1], coords[2][0], coords[2][1])
        diag2 = dist(coords[1][0], coords[1][1], coords[3][0], coords[3][1])
        if diag1 != diag2:
            judge = False
    if judge:
        print(1)
    else:
        print(0)