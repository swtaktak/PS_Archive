import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    brain, zombie = map(int, input().split())
    if brain < zombie:
        print('NO BRAINS')
    else:
        print('MMM BRAINS')