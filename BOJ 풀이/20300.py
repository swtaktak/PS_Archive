import sys
input = sys.stdin.readline

M = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

# 10 40 41 42 
if len(num_list) % 2 == 1:
    max_num = num_list[-1]
    num_list.pop()
else:
    max_num = 0

start = 0
end = len(num_list) - 1
while start < end:
    cur_num = num_list[start] + num_list[end]
    if cur_num > max_num:
        max_num = cur_num
    start += 1
    end -= 1
    
print(max_num)