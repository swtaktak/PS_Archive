import sys
input = sys.stdin.readline

s = str(input().rstrip())
flag = False
answer = 10**18

for start_idx in range(1, min(9, len(s))) :
    cur_start = s[:start_idx]
    cur_digit = len(cur_start) # 공차는 1 이상이라, 확인해아함
    cur_idx = start_idx
    cur_start = int(cur_start)
    if cur_start < 10 ** 9 and s[start_idx] != '0':
    # 2항을 늘리면서 계산한다.
    # 2항으로 등차를 잡고, 나머지를 계산한다.
    # 언제까지? 등차를 실패할까지.
        for second_idx in range(start_idx + 1, len(s)):
            cur_second = int(s[start_idx:second_idx])
            if cur_second == 0 or cur_second > 10 ** 9 or s[second_idx] == '0':
                break
            elif cur_second > cur_start:
                # 등차수열을 만들기 위한 공차 설정정
                gongcha = cur_second - cur_start
                # 항을 더 넘기기 전에, 지금 만으로 가능한가? 3항으로도 되기 때문이다.
                left = int(s[second_idx:])
                if left % cur_second == 0 and left // cur_second >= 2 and left < 10 ** 9:
                    flag = True
                    answer = min(answer, left // cur_second)
                # 3항 이상의 등차가가 가능한가.
                cur_num = cur_second
                cur_idx = second_idx
                while True:
                    next_num = cur_num + gongcha
                    next_len = len(str(next_num))
                    # 다음도 등차라면면
                    if next_num < 10 ** 9 and cur_idx + next_len <= len(s) and int(s[cur_idx:cur_idx+next_len]) == next_num:
                        cur_num = next_num
                        cur_idx = cur_idx + next_len
                        if cur_idx != len(s) and s[cur_idx] != '0':
                            left = int(s[cur_idx:])
                            if left % cur_num == 0 and left // cur_num >= 2 and left < 10 ** 9:
                                flag = True
                                answer = min(answer, left // cur_num)
                    else:
                        # 등차에 실패했을 경우, 더 등차가 아니므로.
                        if cur_idx != len(s) and s[cur_idx] != '0':
                            left = int(s[cur_idx:])
                            if left % cur_num == 0 and left // cur_num >= 2 and left < 10 ** 9:
                                flag = True
                                answer = min(answer, left // cur_num)
                        break
if not flag:
    print(0)
else:
    print(int(answer))