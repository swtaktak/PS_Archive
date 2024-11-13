import sys
input = sys.stdin.readline

num_list = [0] * 101
for i in range(1, 101):
    if i == 1:
        num_list[i] = 1
    elif i == 2:
        num_list[i] = 1
    elif i == 3:
        num_list[i] = 1
    else:
        num_list[i] = num_list[i-2] + num_list[i-3]

t_case = int(input())

for _ in range(t_case):
    N = int(input())
    print(num_list[N])