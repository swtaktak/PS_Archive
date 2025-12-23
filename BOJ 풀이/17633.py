import sys
input = sys.stdin.readline

N = int(input())

if int(N ** 0.5) ** 2 == N:
    print(1)
else:
    # N을 소인수 분해를 해야 한다....
    judge = True
    
    
    if judge:
        print(2)
    else:
        cur = N
        while cur % 4 == 0:
            cur //= 4
        if cur % 8 != 7:
            print(3)
        else:
            print(4)