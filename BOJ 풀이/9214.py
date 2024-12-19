import sys
input = sys.stdin.readline
cur_case = 1
while True:
    N = int(input())
    if N == 0:
        break
    else:
        answer = str(N)
        while True:
            if len(answer) % 2 == 1:
                break
            else:
                next_answer = ''
                fail_flag = False
                for i in range(0, len(answer), 2):
                    if i == 0:
                        cur_cnt = answer[i]
                        cur_type = answer[i+1]
                        next_answer += (cur_type) * (int(cur_cnt))
                        prev_type = cur_type
                    else:
                        cur_cnt = answer[i]
                        cur_type = answer[i+1]
                        if cur_type == prev_type:
                            fail_flag = True
                            break
                        else:
                            next_answer += (cur_type) * (int(cur_cnt))
                            prev_type = cur_type
                if fail_flag:
                    break
                if next_answer == answer:
                    break
                answer = next_answer
        print("Test %d: %d" %(cur_case, int(answer)))
        cur_case += 1