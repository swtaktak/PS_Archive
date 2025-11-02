import sys
input = sys.stdin.readline
N = int(input())
x_axis = []
y_axis = []

for _ in range(N):
    cx, cy = map(int, input().split())
    if cy == 0:
        x_axis.append(cx)
    else:
        y_axis.append(cy)
        
if len(x_axis) < 2 or len(y_axis) == 0:
    print(0)
else:
    abs_y = [abs(y) for y in y_axis]
    answer = max(abs_y) * (max(x_axis) - min(x_axis)) * 0.5
    print(answer)