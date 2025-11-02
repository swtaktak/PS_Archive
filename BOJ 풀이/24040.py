import sys
input = sys.stdin.readline
def solve(N):
    if N % 3 == 0:
        if N % 9 == 0:
            print('TAK')
        else:
            print('NIE')
    elif N % 3 == 2:
        print('TAK')
    else:
        print('NIE')

T = int(input())
for _ in range(T):
    N = int(input())
    solve(N)