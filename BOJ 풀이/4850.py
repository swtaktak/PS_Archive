# 4850

import sys
input = sys.stdin.readline

while True:
    
    try:
        basket, right, diff, cur_weight = list(map(int, input().split()))
    except:
        break
    
    coins = basket * (basket-1) // 2
    right_weight = coins * right
    weight_diff = right_weight - cur_weight
    
    if weight_diff == 0:
        print(basket)
    else:
        print(weight_diff // diff)
    