import sys
input = sys.stdin.readline

ioi_N = int(input())
str_len = int(input())
chk_str = str(input().rstrip())
answer = 0

cur_pos = 0
count_ioi = 0
# 더 볼 필요도 없는 위치까지만 진행한다.
while cur_pos < str_len-1:
    if chk_str[cur_pos : cur_pos + 3] == 'IOI':
        count_ioi += 1
        cur_pos += 2
        if count_ioi == ioi_N:
            answer += 1
            count_ioi -= 1
    else:
        cur_pos += 1
        count_ioi = 0
print(answer)