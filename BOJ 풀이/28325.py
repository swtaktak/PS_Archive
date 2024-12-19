import sys
input = sys.stdin.readline
N = int(input())
sub_cave = list(map(int, input().split()))

answer = 0
sub_idx = []
# 그리디하게, 쪽방엔 모두 가둬둔다.
for i in range(N):
    if sub_cave[i] > 0:
        answer += sub_cave[i]
        sub_idx.append(i)
# 쪽방이 하나도 없을 경우
if answer == 0:
    answer = N // 2
# 쪽방이 있을 경우
else:
    sub_idx.append(sub_idx[0] + N)
    for i in range(1, len(sub_idx)):
        answer += ((sub_idx[i] - sub_idx[i-1])//2)
print(answer)