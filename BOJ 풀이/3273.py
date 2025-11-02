import sys
input = sys.stdin.readline
N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
target = int(input())

ans = 0
start = 0
end = N - 1

while start < end:
    cur_sum = num_list[start] + num_list[end]
    if cur_sum > target:
        end -= 1
    elif cur_sum < target:
        start += 1
    else:
        ans += 1
        start += 1
print(ans)