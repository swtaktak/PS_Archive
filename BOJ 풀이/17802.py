import sys
input = sys.stdin.readline
line, N = map(int, input().split())
dp = [[] for _ in range(line + 1)]

fail_flag = False
for i in range(1, line + 1):
    if i == 1:
        dp[i].append(N)
    else:
        start_num = dp[i-1][0] // 2
        if start_num == 0:
            fail_flag = True
            break
        dp[i].append(start_num)
        for j in range(0, i-1):
            if dp[i-1][j] - dp[i][-1] <= 0:
                fail_flag = True
                break
            dp[i].append(dp[i-1][j] - dp[i][-1])
        # 마지막에 문제가 생겼을 가능성이 높음, 앞을 뒤집어서 시도하자.
        if fail_flag and dp[i-1][0] % 2 == 1:
            # 재시도, 뒤집어서서
            fail_flag = False
            dp[i] = []
            start_num = dp[i-1][0] // 2 + 1
            dp[i].append(start_num)
            for j in range(0, i-1):
                if dp[i-1][j] - dp[i][-1] <= 0:
                    fail_flag = True
                    break
        if fail_flag:
            break        
if fail_flag:
    print(dp)
    print('impossible')
else:
    for i in range(1, line + 1):
        cur_row = dp[i]
        for c in cur_row:
            print(c, end = " ")
        print()