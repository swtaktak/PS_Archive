import sys
import math
input = sys.stdin.readline
p = 10 ** 9 + 7

coms = int(input())
fee_list = []
for _ in range(coms):
    w, h = map(int, input().split())
    fee = w * h * 96 // 60000
    fee_list.append(fee)
lb, ub = map(int, input().split())

# upper bound 까지만 경계를 만들자.
dp = [[0 for _ in range(ub + 1)] for _ in range(coms)]

for i in range(coms):
    cur_fee = fee_list[i]
    if i == 0:
        if cur_fee <= ub:
            dp[i][cur_fee] = 1
    else:
        # 우선 지금 거는 추가를 하고. 과거 가능성도 더해주자.
        if cur_fee <= ub:
            dp[i][cur_fee] += 1
        for j in range(0, ub + 1, 6):
            if j-cur_fee >= 0:
                dp[i][j] += (dp[i-1][j] + dp[i-1][j-cur_fee]) % p
            else:
                dp[i][j] += dp[i-1][j] % p
answer = 0
new_lb = math.ceil(lb / 6) * 6
for i in range(lb, ub + 1):
    answer += dp[-1][i]
print(answer % p)