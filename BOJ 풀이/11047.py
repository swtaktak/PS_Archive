coins, money = map(int, input().split())
coin_list = []
for i in range(coins):
    cur_coin = int(input())
    coin_list.append(cur_coin)
    
min_coin = 0
for i in range(coins-1, -1, -1):
    cur_coin = coin_list[i]
    min_coin += money // cur_coin
    money = money % cur_coin

print(min_coin)