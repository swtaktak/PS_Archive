import sys
input = sys.stdin.readline

N = int(input())
min_list = [0, 0, 0]
max_list = [0, 0, 0]

for i in range(0, N):
    cur_list = list(map(int, input().split()))
    
    min_list = (cur_list[0] + min(min_list[0], min_list[1]),
                cur_list[1] + min(min_list),
                cur_list[2] + min(min_list[1], min_list[2]))
    
    max_list = (cur_list[0] + max(max_list[0], max_list[1]),
                cur_list[1] + max(max_list),
                cur_list[2] + max(max_list[1], max_list[2]))
    
min_result = min(min_list)
max_result = max(max_list)

print("%d %d" %(max_result, min_result))