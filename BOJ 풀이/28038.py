import sys
import math
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    mode = int(input())
    if mode == 1:
        cx, cy = map(float, input().split())
        dist = math.sqrt(cx ** 2 + cy ** 2)
        theta = math.atan2(cy, cx)
        if theta < 0:
            theta += 2 * math.pi  # 0 ≤ theta < 2π 보장
        print("%.8f %.8f" % (dist, theta))
    else:
        cr, ct = map(float, input().split())
        cx = cr * math.cos(ct)
        cy = cr * math.sin(ct)
        print("%.8f %.8f" % (cx, cy))
