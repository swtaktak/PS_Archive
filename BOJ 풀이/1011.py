import sys
input = sys.stdin.readline
# N(N+1) 형태에 주의.
T = int(input())
for _ in range(T):
    start, end = map(int, input().split())
    dist = end-start
    if dist <= 3:
        print(dist)
    elif int(dist ** 0.5) ** 2 == dist:
        print(int(dist ** 0.5) * 2 - 1)
    elif dist <= int(dist ** 0.5) + int(dist ** 0.5) ** 2:
        print(int(dist ** 0.5) * 2)
    else:
        print(int(dist ** 0.5) * 2 + 1)