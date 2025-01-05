import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cur_num = int(input())
    digit = len(str(cur_num))
    # 빼면 9가 생긴다. 9가 몇개 필요해?
    new_num = cur_num * (10 ** digit) - cur_num
    
    digit_sum = 0
    for n in str(new_num):
        digit_sum += int(n)
    if digit_sum % 2 != 0:
        print(new_num)
    else:
        print(cur_num * (10 ** (digit + 1)) - cur_num)