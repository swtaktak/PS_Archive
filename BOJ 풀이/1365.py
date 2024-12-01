# 꼬인 전깃줄
# LCS?
import sys
input = sys.stdin.readline
N = int(input())
def binary_input(num):
    left = 0
    right = len(cur_list) 
    while left < right:
        mid = (left + right) // 2
        if cur_list[mid] <= num:
           left += 1
        else:
           right = mid
    return right

cur_list = [0]
line_list = list(map(int, input().split()))
for l in line_list:
    pos = binary_input(l)
    print(pos)
    if pos < len(cur_list):
        cur_list[pos] = l
    else:
        cur_list.append(l)
    print(cur_list)
print(N - (len(line_list) - 1))