import sys
input = sys.stdin.readline
P = 10 ** 9 + 7

N = int(input())

if N == 0:
    ans = 1
else:
    ans = pow(2, N-1, P)
print(ans)