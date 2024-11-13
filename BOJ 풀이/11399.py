num = int(input())
time_list = list(map(int, input().split()))
time_list.sort()
sum_time = 0
for i in range(0, num):
    sum_time += ((num-i) * time_list[i])
print(sum_time)