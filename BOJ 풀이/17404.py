import sys
input = sys.stdin.readline

INF = 1e9
house = int(input())
red_dp = [0, 0, 0]
green_dp = [0, 0, 0]
blue_dp = [0, 0, 0]
answer = 1e9

cost_list = []
for _ in range(house):
    cost_list.append(list(map(int, input().split())))
for k in range(3):
    # 최초의 색깔을 가져가서 기억하고 각 색별로 dp를 돌린다.
    first_color = cost_list[0][k]
    dp = [0, 0, 0]
    for i in range(1, house):
        # 최초 색깔을 지정하고 dp를 진행
        if i == 1:
            for j in range(3):
                if j == k:
                    dp[j] = INF
                else:
                    dp[j] = cost_list[i][j] + first_color
        else:
            last_dp = dp.copy()
            dp[0] = min(cost_list[i][0] + last_dp[1], cost_list[i][0] + last_dp[2])
            dp[1] = min(cost_list[i][1] + last_dp[0], cost_list[i][1] + last_dp[2])
            dp[2] = min(cost_list[i][2] + last_dp[0], cost_list[i][2] + last_dp[1])
    if k == 0: 
        cur_answer = min(dp[1], dp[2])
        answer = min(answer, cur_answer)
    if k == 1: 
        cur_answer = min(dp[0], dp[2])
        answer = min(answer, cur_answer)
    if k == 2: 
        cur_answer = min(dp[0], dp[1])
        answer = min(answer, cur_answer)
print(answer)            