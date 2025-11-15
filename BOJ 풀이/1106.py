import sys
input = sys.stdin.readline
INF = 1000 * 100 + 1
customer, city = map(int, input().split())


cost_dict = {}
get_custom_list = [] # 얻을 수 있는 고객 수 단위 목록
for _ in range(city):
    cur_cost, cur_custom = map(int, input().split())
    if cur_custom not in cost_dict:
        cost_dict[cur_custom] = cur_cost
        get_custom_list.append(cur_custom)
    else:
        cost_dict[cur_custom] = min(cur_cost, cost_dict[cur_custom])

get_custom_list.sort()
dp = [INF for _ in range(customer + 1 + get_custom_list[-1])]
dp[0] = 0    


for i in range(get_custom_list[0], len(dp)):
    cur_cost = INF
    for cur_custom in get_custom_list:
        if cur_custom > i:
            break
        else:
            cur_cost = min(cur_cost, dp[i-cur_custom] + cost_dict[cur_custom])
    dp[i] = cur_cost
    
print(min(dp[customer:]))