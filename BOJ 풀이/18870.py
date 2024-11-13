import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
sorted_list = sorted(num_list)
rnk_dict = {}

# 사실 이렇게 안하고 걍 집합으로 만들면 더 효율적이었음.
cur_rnk = 0
for i in range(0, N):
    if sorted_list[i] not in rnk_dict:
        rnk_dict[sorted_list[i]] = cur_rnk
        cur_rnk += 1

for i in range(0, N):
    if i < N-1:
        print(rnk_dict[num_list[i]], end=" ")
    else:
        print(rnk_dict[num_list[i]])