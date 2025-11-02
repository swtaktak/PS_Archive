# 편차의 누적합의 절댓값

import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
cutline = sum(num_list) // N
max_idx = num_list.index(max(num_list))
num_list = num_list[max_idx:]+num_list[:max_idx]
num_list_rev = [num_list[0]] + num_list[1:][::-1]
diff_list = []
diff_list_rev = []

for i in range(N):
    if i == 0:
        diff_list.append(num_list[i] - cutline)
        diff_list_rev.append(num_list_rev[i] - cutline)
    else:
        diff_list.append(diff_list[-1] + num_list[i] - cutline)
        diff_list_rev.append(diff_list_rev[-1] + num_list_rev[i] - cutline)

print(diff_list)
abs_diff_list = [abs(x) for x in diff_list]
abs_diff_list_rev = [abs(x) for x in diff_list_rev]
print(min(sum(abs_diff_list), sum(abs_diff_list_rev)))
