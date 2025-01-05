import sys
input = sys.stdin.readline

answer = []
while True:
    cur_line = str(input().rstrip())
    if cur_line == '#':
        break
    else:
        if cur_line == '*':
            # padding 위함.
            answer.append(2)
        else:
            space_cnt = 0
            for c in cur_line:
                if c == ' ':
                    space_cnt += 1
                else:
                    if space_cnt > 0:
                        if space_cnt % 2 == 1:
                            answer.append(0)
                        else:
                            answer.append(1)
                        space_cnt = 0
            if space_cnt > 0:
                answer.append(space_cnt)
# answer을 두고 이제 변환을 실시한다.
cur_stack = []
ans_list = []
for a in answer:
    if a != 2:
        cur_stack.append(a)
    else:
        while len(cur_stack) % 5 != 0:
            cur_stack.append(0)
        cur_ans = ''
        for i in range(0, len(cur_stack), 5):
            cur_p = cur_stack[i:i+5]
            cur_code = cur_p[0] * 16 + cur_p[1] * 8 + cur_p[2] * 4 + cur_p[3] * 2 + cur_p[4] * 1
            if cur_code == 0:
                cur_ans += " "
            elif cur_code == 27:
                cur_ans += "\'"
            elif cur_code == 28:
                cur_ans += ','
            elif cur_code == 29:
                cur_ans += '-'
            elif cur_code == 30:
                cur_ans += '.'
            elif cur_code == 31:
                cur_ans += '?'
            else:
                cur_ans += chr(cur_code + 64)
        ans_list.append(cur_ans)
        cur_stack = []
for a in ans_list:
    print(a)