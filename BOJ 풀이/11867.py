import sys
input = sys.stdin.readline

a,b = map(int, input().split())
if a % 2 == 1 and b % 2 == 1:
    print('B')
else:
    print('A')