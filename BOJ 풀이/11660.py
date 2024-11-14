import sys
input = sys.stdin.readline

N, t_case = map(int, input().split())
num_table = []
for _ in range(N):
    cur_row = list(map(int, input().split()))
    num_table.append(cur_row)

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if j == 0:
            # 각 행의 첫번째 열일 경우는 그냥 위에서 더한다.
            # 첫번째 행일 경우는 그냥 입력, 두 번째 행부터는 누적합을 실시.
            if i == 0:
                dp[i][j] = num_table[0][0]
            else:
                dp[i][j] = num_table[i][0] + dp[i-1][0]
            cur_row_sum = num_table[i][0]
        else:
            # 두 번째 열부터에 대한 정보
            if i == 0:
                dp[i][j] = cur_row_sum + num_table[i][j]
                cur_row_sum += num_table[i][j]
            else:
                dp[i][j] = cur_row_sum + dp[i-1][j] + num_table[i][j]
                cur_row_sum += num_table[i][j]

for _ in range(t_case):
    sx, sy, ex, ey = map(int, input().split())
    
    result_sum = dp[ex-1][ey-1]
    # 여기서 필요 없는 부분을 빼 간다. 겹치는 부분은 다시 더하는 포함배제의 원리 활용
    if sx - 2 >= 0:
        result_sum -= dp[sx-2][ey-1]
    if sy - 2 >= 0:
        result_sum -= dp[ex-1][sy-2]
    if sx - 2 >= 0 and sy -2 >= 0:
        result_sum += dp[sx-2][sy-2]
    print(result_sum)