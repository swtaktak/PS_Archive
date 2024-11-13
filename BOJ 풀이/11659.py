import sys
input = sys.stdin.readline

num, t_case = map(int, input().split())
sum_list = [0] * (num + 1)
cur_sum = 0
num_list = list(map(int, input().split()))
for i in range(1, num+1):
    cur_sum += num_list[i-1]
    sum_list[i] = cur_sum
    
# 0 5 9 12 14 15
for _ in range(t_case): 
    s, e = map(int, input().split())
    print(sum_list[e]-sum_list[s-1])