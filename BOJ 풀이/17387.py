# 선분 교차
# 많조분? 단순하게?
import sys
input = sys.stdin.readline

def judge(a, b, c, d):
    # step 1. 방향 정리
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    # step 2. c, d 입장에서 a, b 정리
    if a == b:
        if c <= a <= d:
            return True
        else:
            return False
    else:
        if a <= c <= b or a <= d <= b:
            return True
        else:
            return False
    

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

if judge(x1, x2, x3, x4) and judge(y1, y2, y3, y4):
    print(1)
else:
    print(0)