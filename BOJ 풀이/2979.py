import sys
input = sys.stdin.readline
cost_list = [0] + list(map(int, input().split()))
truck_1 = [0] * 101
truck_2 = [0] * 101
truck_3 = [0] * 101

start_1, end_1 = map(int, input().split())
start_2, end_2 = map(int, input().split())
start_3, end_3 = map(int, input().split())
for i in range(start_1, end_1):
    truck_1[i] = 1
for i in range(start_2, end_2):
    truck_2[i] = 1
for i in range(start_3, end_3):
    truck_3[i] = 1

answer = 0
for i in range(1, 101):
    cur_hour = truck_1[i] + truck_2[i] + truck_3[i]
    answer += cost_list[cur_hour] * cur_hour
print(answer)