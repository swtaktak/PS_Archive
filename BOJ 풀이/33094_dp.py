import sys
from collections import deque

input = sys.stdin.readline
days, milk, cookie = map(int, input().split())
need_milk = [0] + list(map(int, input().split()))

dp = [[] for _ in range(days + 1)]
if cookie == 0 and need_milk[1] > milk:
    print(0)
else:
    fail_flag = False
    for cur_day in range(1, days + 1):
        if cur_day == 1:
            if cookie > 0:
                dp[1].append([milk, cookie - 1])
            if milk >= need_milk[1]:
                dp[1].append([milk - need_milk[1], cookie])
        else:
            prev_list = dp[cur_day - 1]
            for prev in prev_list:
                prev_milk = prev[0]
                prev_cookie = prev[1]
                if prev_cookie > 0:
                    dp[cur_day].append([prev_milk, prev_cookie - 1])
                if prev_milk >= need_milk[cur_day]:
                    dp[cur_day].append([prev_milk - need_milk[cur_day], prev_cookie])
            if len(dp[cur_day]) == 0:
                fail_flag = True
                break
    if fail_flag:
        print(cur_day - 1)
    else:
        print(days)