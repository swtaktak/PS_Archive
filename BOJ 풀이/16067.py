# 최대공약수가 아님
# 1로 끝나야 한다.

import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
max_num = max(num_list)

# 32항 정도면 충분
dp_list = [0 for _ in range(32)]
dp_list[0] = 1
dp_list[1] = 1
for i in range(2, 32):
    dp_list[i] = dp_list[i-1] + dp_list[i-2]

card_list = {}
for i in range(N):
    if num_list[i] not in card_list:
        card_list[num_list[i]] = [i + 1]
    else:
        card_list[num_list[i]].append(i + 1)

judge = False
for i in range(1, 32):
    pow_left = dp_list[i-1]
    pow_right = dp_list[i]
    
    if pow_right > max_num:
        break
    
    elif pow_left == 1 and pow_right == 1:
        if 1 in card_list and len(card_list[1]) >= 2:
            judge = True
            ans_l = card_list[1][0]
            ans_r = card_list[1][1]
            break
    else:
        if pow_left in card_list and pow_right in card_list:
            judge = True
            ans_l = card_list[pow_left][0]
            ans_r = card_list[pow_right][0]
            break
if judge:
    print("%d %d" %(ans_l, ans_r))
else:
    print("impossible")