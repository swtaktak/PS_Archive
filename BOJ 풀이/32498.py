import sys
input = sys.stdin.readline

N = int(input())
ans = 0

for _ in range(N):
    cur_diff = int(input())
    if cur_diff % 2 == 1:
        ans += 1
print(ans)