import sys
input = sys.stdin.readline
area = 0
max_y = 0

coord = []
N = int(input())
for _ in range(N):
    cx, cy = map(int, input().split())
    coord.append([cx//2, cy//2])
coord.sort(key = lambda x: -x[0])

for i in range(N):
    cx, cy = coord[i][0], coord[i][1]
    if max_y < cy:
        area += ((cy - max_y) * cx)
        max_y = cy

print(area * 4)