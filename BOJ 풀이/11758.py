# ccw algorithm
import sys
input = sys.stdin.readline
def ccw(x1, y1, x2, y2, x3, y3):
    det = (x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1)
    if det > 0:
        return 1 # 반시계
    elif det < 0 :
        return - 1 # 시계
    else:
        return 0 # 직선
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
print(ccw(x1, y1, x2, y2, x3, y3))