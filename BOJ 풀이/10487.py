import sys
from collections import deque
input = sys.stdin.readline

def cal(cur_op):
    q = deque()
    i = 0
    while i < len(cur_op):
        if i == 0:
            q.append(cur_op[i])
            i += 1
        else:
            if cur_op[i] not in ops:
                #  숫자는 큐에 그대로 담는다.
                q.append(cur_op[i])
                i += 1
            else:
                # 기호를 담는 경우
                if cur_op[i] in ['+', '-']:
                    # 더하기 빼기는 마지막에 계산할 것
                    q.append(cur_op[i])
                    i += 1
                else:
                    # 곱하기 나누기의 경우에는 우선적으로 먼저 계산한다.
                    # 단, 여기서 나누기는 일반적인 나누기는 아니다.  기호는 /인데, 연산은 //이다.
                    prev_num = q.pop()
                    op = cur_op[i]
                    next_num = cur_op[i+1]
                    if op == '*':
                        result_num = prev_num * next_num
                    elif op == '/':
                        result_num = prev_num // next_num
                    q.append(result_num)
                    i += 2

    result = q.popleft()
    while q:
        op = q.popleft()
        next_num = q.popleft()
        if op == '+':
            result += next_num
        elif op == '-':
            result -= next_num            
    return result


ops = ['+', '-', '*', '/']
result = {}
for c1 in ops:
    for c2 in ops:
        for c3 in ops:
            cur_op = [4, c1, 4, c2, 4, c3, 4]
            get_ans = cal(cur_op)
            if get_ans not in result:
                result[get_ans] = [c1, c2, c3]

T = int(input())
for _ in range(T):
    N = int(input())
    if N in result:
        c1, c2, c3 = result[N]
        print("4 %s 4 %s 4 %s 4 = %d" %(c1, c2, c3, N))
    else:
        print("no solution")