import sys
input = sys.stdin.readline


left, keep = map(int, input().split())
num_list = list(map(int, input().split()))

ans = 0
cur = 0
for i in range(left):
    if i < keep:
        cur += num_list[i]
    else:
        cur += num_list[i]
        cur -= num_list[i - keep]
    if 129 <= cur <= 138:
        ans += 1
print(ans)