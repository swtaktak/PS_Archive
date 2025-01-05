import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    num = int(input())
    if num % 9 != 0:
        print(-1)
    else:
        digit = len(str(num))
        ans = 0
        cur_num = num
        fail_flag = False
        for i in range(digit, 0, -1):
            cur_seed = int('9' * i)
            if cur_num // cur_seed == 10:
                fail_flag = True
                break
            else:
                ans += ((10 ** i) * (cur_num // cur_seed))
                cur_num = cur_num % cur_seed
        if fail_flag:
            print(-1)
        else:
            print(ans)