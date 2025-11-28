# 2502
# 간단한 역피보나치 문제
# a, b, a+b, a+2b,

import sys
input = sys.stdin.readline
day, rice_cake = map(int, input().split())

dp = [[0, 0] for _ in range(day)]
for i in range(day):
    if i == 0:
        dp[i][0] = 1
        dp[i][1] = 0
    elif i == 1:
        dp[i][0] = 0
        dp[i][1] = 1
    else:
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

# 3a + 5b = 41
a = dp[-1][0] # 
b = dp[-1][1] # 

day2 = rice_cake // b
for cur_day2 in range(day2, 0, -1):
    if (rice_cake - b * cur_day2) % a == 0 and (rice_cake - b * cur_day2) // a > 0:
        print((rice_cake - b * cur_day2) // a)
        print(cur_day2)
        break
