import sys
input = sys.stdin.readline
x_list = []
y_list = []

N = int(input())

for _ in range(N):
    cx, cy = map(int, input().split())
    x_list.append(cx)
    y_list.append(cy)

x_list.sort()
y_list.sort()
mid = (N-1) // 2
mx = x_list[mid]
my = y_list[mid]

ans = 0
for i in range(N):
    ans += abs(x_list[i] - mx)
    ans += abs(y_list[i] - my)
print(int(ans))