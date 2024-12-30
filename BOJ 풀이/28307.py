import sys
input = sys.stdin.readline

N = int(input())
line_up = list(map(int, input().split()))
line_down = list(map(int, input().split()))
ans = 0
# 윗줄 대각선
for i in range(1, N):
    if line_up[i] != line_up[i-1]:
        ans += 1
if line_up[0] == 1:
    ans += 1
if line_up[-1] == 1:
    ans += 1

# 아랫줄 대각선
for i in range(1, N):
    if line_down[i] != line_down[i-1]:
        ans += 1
if line_down[0] == 1:
    ans += 1
if line_down[-1] == 1:
    ans += 1

# 중간줄
for i in range(0, N, 2):
    if line_up[i] != line_down[i]:
        ans += 1

# 윗줄/아랫줄줄
for i in range(1, N, 2):
    if line_up[i] == 1:
        ans += 1
    if line_down[i] == 1:
        ans += 1
print(ans)