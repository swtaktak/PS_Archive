# 구분자가 여러개일 경우의 대처법
# re 정규 표현식 문제
import sys
import re
input = sys.stdin.readline

expression = str(input().rstrip())
expression = re.split('([-+])', expression)

minus_flag = False
result_num = []
for cur_exp in expression:
    if cur_exp == '-':
        minus_flag = True
    elif cur_exp != '+':
        # 숫자이므로 계산
        cur_num = int(cur_exp)
        if minus_flag:
            result_num.append(cur_num * -1)
        else:
            result_num.append(cur_num)
print(sum(result_num))