import sys
input = sys.stdin.readline

num, turn = map(int, input().split())
num_list = list(map(int, input().split()))
answer = -1
cw_cum = 0
ccw_cum = 0

for cur_pos in range(min(num, turn)):
    answer = max(answer, cw_cum + (turn - cur_pos) * num_list[cur_pos])
    cw_cum += num_list[cur_pos]

num_list = num_list[::-1]

for cur_pos in range(min(num, turn)):
    answer = max(answer, ccw_cum + (turn - cur_pos) * num_list[cur_pos])
    ccw_cum += num_list[cur_pos]
    
print(answer)