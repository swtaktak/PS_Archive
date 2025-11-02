import sys
input = sys.stdin.readline

a, k = map(int, input().split())
if a == 1:
    print(1)
else:
    if k == 0:
        print(a)
    else:
        if a % 2 == 0:
            print(1)
        else:
            print(a)