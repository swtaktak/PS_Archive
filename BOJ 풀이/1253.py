import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

answer = 0
for i in range(N):
    target = num_list[i]
    
    start = 0
    end = N-1
    
    while start < end:
        cur_sum = num_list[start] + num_list[end]
        if cur_sum == target:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                answer += 1
                break
        elif cur_sum > target:
            end -= 1
        elif cur_sum < target:
            start += 1
if N <= 2:
    print(0)
else:
    print(answer)