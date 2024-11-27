import sys
input = sys.stdin.readline

coin, amt = map(int, input().split())
coin_list = []
for _ in range(coin):
    cur_coin = int(input())
    if cur_coin not in coin_list:
        coin_list.append(cur_coin)
        
coin_list.sort()

if amt < coin_list[0]:
    print(-1)
else:
    dp = [-1] * (amt + 1) # 불가능 케이스 고려를 위한 -1 처리
    for i in range(coin_list[0], amt+1):
        if i == coin_list[0]:
            dp[i] = 1
        else:
            if i in coin_list:
                dp[i] = 1
            else:
                min_coin = 100001
                for c in coin_list:
                    if i-c >= 0 and dp[i-c] > 0:
                        min_coin = min(min_coin, dp[i-c] + 1)
                if min_coin != 100001:
                    dp[i] = min_coin
print(dp[-1])