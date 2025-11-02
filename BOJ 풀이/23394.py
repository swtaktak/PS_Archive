# 색별로 정렬하기
import sys
input = sys.stdin.readline
nums, colors = map(int, input().split())
block_list = [[] for _ in range(colors + 1)]
color_seq = []

for _ in range(nums):
    cur_num, cur_color = map(int, input().split())
    block_list[cur_color].append(cur_num)
    color_seq.append(cur_color)
for i in range(1, colors + 1):
    block_list[i] = sorted(block_list[i], reverse = True)

ans_list = []
for c in color_seq:
    ans_list.append(block_list[c].pop())

if ans_list == sorted(ans_list):
    print('Y')
else:
    print('N')
    