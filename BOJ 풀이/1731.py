import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

# 자연수 범위는 바로 판단됨
if num_list[1] * 2 == num_list[0] + num_list[2]:
    diff = num_list[1] - num_list[0]
    print(num_list[-1] + diff)
else:
    rad = num_list[1] // num_list[0]
    print(num_list[-1] * rad)