import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())

    if a < b and b % a == 0:
        print(1)
    else:
        print(0)