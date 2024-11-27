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
    print(0)
else:
    dp_list = [0] * (amt + 1)
    dp_list[0] = 1
    for i in range(len(coin_list)):
        cur_coin = coin_list[i]
        if i == 0:
            for j in range(cur_coin, amt+1, cur_coin):
                dp_list[j] = 1
        else:
            for j in range(cur_coin, amt + 1):
                dp_list[j] = dp_list[j] + dp_list[j - cur_coin]
    print(dp_list[-1])