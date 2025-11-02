import sys
input = sys.stdin.readline

s = str(input().rstrip())
flag = False
answer = 10 ** 18

for start_idx in range(1, min(10, len(s))):
    cur_start = int(s[:start_idx])
    if cur_start < 10 ** 9 and s[start_idx] != '0':
        for second_idx in range(start_idx + 1, len(s)):
            if s[second_idx] != '0':
                cur_second = int(s[start_idx:second_idx])
                if cur_second < 10 ** 9 and cur_second > cur_start:
                    gongcha = cur_second - cur_start
                    left_num = int(s[second_idx:])
                    if left_num % cur_second == 0 and left_num // cur_second >= 2 and left_num < 10 ** 9:
                        flag = True
                        answer = min(answer, left_num // cur_second)
                    cur_num = cur_second
                    cur_idx = second_idx
                    while True:
                        next_num = cur_num + gongcha
                        next_len = len(str(next_num))
                        if next_num < 10 ** 9 and cur_idx + next_len <= len(s) and int(s[cur_idx:cur_idx+next_len]) == next_num:
                            cur_num = next_num
                            cur_idx = cur_idx + next_len
                            if cur_idx != len(s) and s[cur_idx] != '0':
                                left_num = int(s[cur_idx:])
                                if left_num % cur_num == 0 and left_num // cur_num >= 2 and left_num < 10 ** 9:
                                    flag = True
                                    answer = min(answer, left_num // cur_num)
                        else:
                            if cur_idx != len(s) and s[cur_idx] != '0':
                                left_num = int(s[cur_idx:])
                                if left_num % cur_num == 0 and left_num // cur_num >= 2 and left_num < 10 ** 9:
                                    flag = True
                                    answer = min(answer, left_num // cur_num) 
                            break
if not flag:
    print(0)
else:
    print(int(answer))