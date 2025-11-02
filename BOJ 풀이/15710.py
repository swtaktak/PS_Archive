import sys
input = sys.stdin.readline
a, b, n = map(int, input().split())
p = 10 ** 9 + 7
ans = pow(2 ** 31, n - 1, p)
print(ans)