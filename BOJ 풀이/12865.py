# 배낭 문제 풀이.
import sys
input = sys.stdin.readline
items, weight_limit = map(int, input().split())
item_list = []
# 열을 맞추기 위한 작업.
item_list.append([])

for _ in range(items):
    cur_w, cur_v = map(int, input().split())
    item_list.append([cur_w, cur_v])

dp = [[0 for _ in range (weight_limit + 1)] for _ in range(items + 1)]

for i in range(1, items + 1):
    # 현재의 아이템에 대해 판정한다.
    cur_weight, cur_val = item_list[i][0], item_list[i][1]
    for j in range(1, weight_limit + 1):
        # 만일 현재 따지는 아이템이 더 무겁다면? 앞에 데이터.
        if j < cur_weight:
            dp[i][j] = dp[i-1][j]
        # 아니라면 지금의 아이템으로 교체가 더 큰지, 이전이 더 가치가 큰지
        else:
            dp[i][j] = max(dp[i-1][j-cur_weight]+cur_val, dp[i-1][j])
print(dp[items][weight_limit])