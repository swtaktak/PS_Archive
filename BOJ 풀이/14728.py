# 14728
import sys
input = sys.stdin.readline

unit, time = map(int, input().split())

unit_list = [[]]

for _ in range(unit):
    cur_t, cur_s = map(int, input().split())
    unit_list.append([cur_t, cur_s])
    
dp = [[0 for _ in range(time + 1)] for _ in range(unit + 1)]

for cur_unit in range(1, unit + 1):
    cur_time, cur_score = unit_list[cur_unit][0], unit_list[cur_unit][1]
    
    for t in range(0, time + 1):
        if t < cur_time:
            dp[cur_unit][t] = dp[cur_unit - 1][t]
        else:
            dp[cur_unit][t] = max(dp[cur_unit-1][t], dp[cur_unit - 1][t - cur_time] + cur_score)
print(dp[-1][-1])