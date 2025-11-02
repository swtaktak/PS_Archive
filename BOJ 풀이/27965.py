import sys
input = sys.stdin.readline

N, K = map(int, input().split())
ans = 0
for i in range(1, N+1):
    ans = ans * (10 ** len(str(i))) + i
    ans = ans % K

print(ans)