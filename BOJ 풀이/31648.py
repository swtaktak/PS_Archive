import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    n = int(input())
    if n % 10 == 0:
        print('E', end = '\n')
    else:
        print('B', end = '\n')