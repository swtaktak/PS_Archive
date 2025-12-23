import sys
input = sys.stdin.readline

N = int(input())
cnt = [0 for _ in range(N+1)]
num_list = list(map(int, input().split()))

for n in num_list:
    if n <= N:
        cnt[n] += 1

ans = 0
for i in range(N, 0, -1):
    if cnt[i] == i:
        ans = i
        break
if 0 in num_list and ans == 0:
    print(-1)
else:
    print(ans)