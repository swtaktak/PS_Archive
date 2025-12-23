import sys
input = sys.stdin.readline

N = int(input())
if N % 2 == 0:
    # 6k + 2 형태일때 문제.(ex - 8)
    if N % 6 == 2:
        for i in range(2, N + 1, 2):
            print(i)
        print(3)
        print(1)
        for i in range(7, N + 1, 2):
            print(i)
        print(5) 
    else:
        for i in range(2, N + 1, 2):
            print(i)
        for i in range(1, N + 1, 2):
            print(i)
else:
    #6k + 3일때 문제
    if N % 6 == 3:
        for i in range(4, N + 1, 2):
            print(i)
        print(2)
        for i in range(5, N + 1, 2):
            print(i)
        print(1)
        print(3)
    else:
        for i in range(2, N + 1, 2):
            print(i)
        for i in range(1, N + 1, 2):
            print(i)