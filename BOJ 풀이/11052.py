import sys
input = sys.stdin.readline

types = int(input())
price_list = [0] + list(map(int, input().split()))

# 1장을 살 때 최대 금액, 2장을 살 때 최대 금액은 (1장 + 1장, 2장)
# 3장을 살 때의 최대 금액은,  1장 + 2장인지, 3장인지... 어..?
# 반복.
dp = [0 for _ in range(types + 1)]
for cur in range(1, types + 1):
    for cur_buy_add in range(1, cur + 1):
        dp[cur] = max(dp[cur], dp[cur-cur_buy_add] + price_list[cur_buy_add])
print(dp[-1])