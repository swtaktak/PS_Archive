import sys
input = sys.stdin.readline

N = int(input())
card_list = list(map(int, input().split()))
max_val = max(card_list)
card_check = [False] * (max(card_list) + 1)
score_list = [0] * (max(card_list) + 1)
for cur_c in card_list:
    card_check[cur_c] = True

for cur_c in card_list:
    if cur_c == max_val: continue
    else:
        for i in range(2 * cur_c, max_val +1, cur_c):
            if card_check[i]:
                score_list[cur_c] += 1
                score_list[i] -= 1

for c in card_list:
    print(score_list[c], end = " ")