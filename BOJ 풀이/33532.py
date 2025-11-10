import sys
input = sys.stdin.readline
N = int(input())
cnt = 0
while N > 0:
    cnt += (N // 5)
    N = N // 5

print(cnt)