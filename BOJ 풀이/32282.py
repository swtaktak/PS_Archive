import sys
input = sys.stdin.readline

gx, gy, v = map(int, input().split())

dist = (gx ** 2 + gy ** 2) ** 0.5

if dist == int(dist):
    # 정수일 경우
    if dist % v == 0:
        ans = dist // v
    else:
        if dist // v <= 1:
            ans = 2
        else:
            # 삼각부등식의 성질?
            ans = dist // v + 1
else:
    if dist / v <= 1:
        ans = 2
    else:
        ans = int(dist/v) + 1
print(int(ans))