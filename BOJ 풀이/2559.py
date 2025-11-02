import sys
input = sys.stdin.readline

T, D = map(int, input().split())

max_temp = D * (-101)
temp_list = list(map(int, input().split()))
sum_list = [0]
for i in range(0, T):
    if i == 0:
        sum_list.append(temp_list[0])
    else:
        sum_list.append(sum_list[-1] + temp_list[i])
        
for i in range(D, len(sum_list)):
    max_temp = max(sum_list[i] - sum_list[i-D], max_temp)

print(max_temp)