import sys
input = sys.stdin.readline

num, sum_cut = map(int, input().split())
num_list = list(map(int, input().split()))

start = 0
end = 0
min_length = 100001
sum = 0
while True:
    if sum >= sum_cut:
        if end-start < min_length:
            min_length = end-start
        sum -= num_list[start]
        start += 1
    elif end == len(num_list):
        break
    else:
        sum += num_list[end]
        end += 1
if min_length == 100001:
    print(0)
else:    
    print(min_length)