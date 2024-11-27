import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
sum_list = [0] * N

for i in range(N):
    if i == 0:
        sum_list[i] = num_list[i]
    else:
        sum_list[i] = max(num_list[i], sum_list[i-1] + num_list[i])
print(max(sum_list))