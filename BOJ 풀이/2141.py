import sys
input = sys.stdin.readline

# 우체국의 위치를 기준으로 이진탐색을 거리합으로는 불가.
# 단조 함수가 아니기 때문에다.
# 절댓값 거리 함수 합이므로... 인원수가 절반 딱 이상인 최초의 지점에다 박는다.

N = int(input())
pos_dict = {}
people_sum = 0
for _ in range(N):
    cur_pos, cur_num = map(int, input().split())
    if cur_pos not in pos_dict:
        pos_dict[cur_pos] = cur_num
    else:
        pos_dict[cur_pos] += cur_num
    people_sum += cur_num

sorted_pos_dict = sorted(pos_dict.items(), reverse = False)

if people_sum % 2 == 0:
    cutline = people_sum // 2
else:
    cutline = people_sum // 2 + 1
    
sum_people_check = 0
for s in sorted_pos_dict:
    sum_people_check += s[1]
    if sum_people_check >= cutline:
        print(s[0])
        break