# 1744
import sys
input = sys.stdin.readline
zero_cnt = 0
one_cnt = 0
plus_list = []
minus_list = []
new_list = []


N = int(input())
for _ in range(N):
    cur_num = int(input())
    if cur_num > 1:
        plus_list.append(cur_num)
    elif cur_num == 0:
        # 0은 더할 때는 영향이 없으나, 음수를 없애주는 효과를 준다.
        zero_cnt += 1
        # 역시 1도 곱하면 더 작아진다. 주의해야 하지만 없애는 효과도 없어서 분리.
    elif cur_num == 1:
        one_cnt += 1
    else:
        minus_list.append(cur_num)
        
# plus부터 두개씩 처리한다.
if len(plus_list) == 0:
    pass
elif len(plus_list) == 1:
    new_list.append(plus_list[0])
else:
    plus_list.sort(reverse = False)
    while len(plus_list) >= 2:
        num1 = plus_list.pop()
        num2 = plus_list.pop()
        new_list.append(num1 * num2)
    if len(plus_list) == 1:
        new_list.append(plus_list[0])

# 다음은 음수부터 처리한다. 음수는 작은거부터 곱하면 절댓값... 더 커짐
# 음수는 더하면 무조건 작아진다. 무조건 0~1개 남을 때까지 진행
if len(minus_list) == 0:
    pass
elif len(minus_list) >= 2:
    minus_list.sort(reverse = True)
    while len(minus_list) >= 2:
        num1 = minus_list.pop()
        num2 = minus_list.pop()
        new_list.append(num1 * num2)

if len(new_list) == 0:
    cur_sum = 0
else:
    cur_sum = sum(new_list)

if len(minus_list) == 0:
    answer = cur_sum + one_cnt
else: # 무조건 1개가 보장
    if zero_cnt > 0:
        answer = cur_sum + one_cnt
    else:
        answer = cur_sum + one_cnt + minus_list[0]
print(answer)