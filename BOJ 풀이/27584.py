import sys
input = sys.stdin.readline

result_s = str(input().rstrip())
more_win_list = []

for first_k in range(1, len(result_s) + 1):
    a_set_win = 0
    b_set_win = 0
    a_small_win = 0
    b_small_win = 0
    for c in result_s:
        if c == 'A':
            a_small_win += 1
        else:
            b_small_win += 1
        if a_small_win == first_k or b_small_win == first_k:
            if a_small_win == first_k:
                a_set_win += 1
            else:
                b_set_win += 1
            a_small_win = 0
            b_small_win = 0
    if a_set_win > b_set_win:
        more_win_list.append(first_k)

print(len(more_win_list))
if len(more_win_list) > 0:
    for m in more_win_list:
        print(m, end = " ")