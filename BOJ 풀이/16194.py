import sys
input = sys.stdin.readline

buy = int(input())
price = [0] + list(map(int, input().split()))
dp = [0] * (buy + 1)

for i in range(1, buy + 1):
    if i == 1:
        dp[i] = price[1]
    else:
        cur_list = []
        # price[10]
        # dp[1] + price[9]
        #...
        # dp[9] + price[1]
        
        # 1 2 3 ... buy - 1
        for j in range(1, i):
            cur_list.append(dp[j] + price[i-j])
        cur_list.append(price[i])
        dp[i] = min(cur_list)
print(dp[-1])