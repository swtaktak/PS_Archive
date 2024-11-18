# 보물
# 큰거를 가장 작은거랑 곱하게.

import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
sum = 0

a.sort(reverse = True)
b.sort(reverse = False)
for i in range(N):
    sum += a[i] * b[i]
print(sum)