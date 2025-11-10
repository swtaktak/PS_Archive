import sys
input = sys.stdin.readline

N, diff_cut = map(int, input().split())

num_list = []

for _ in range(N):
    num_list.append(int(input()))

num_list.sort()
start = 0
end = 0
min_diff = int(2e9) + 1

while end < N:
    cur_diff = num_list[end] - num_list[start]
    if cur_diff == diff_cut:
        min_diff = cur_diff
        break
    elif cur_diff < diff_cut:
        end += 1
    else:
        min_diff = min(min_diff, cur_diff)
        start += 1
print(min_diff)