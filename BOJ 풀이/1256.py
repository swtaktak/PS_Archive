import sys
input = sys.stdin.readline

# nCk  table을 먼저 만들자.
dp = [[0 for _ in range(201)] for _ in range(201)]

for i in range(201):
    if i == 0:
        dp[i][i] = 1
    else:
        for j in range(0, i + 1):
            if j == 0 or j == i:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


a_cnt, z_cnt, goal = map(int, input().split())
answer = ''
cur_a, cur_z = a_cnt, z_cnt

if dp[a_cnt+z_cnt][z_cnt] < goal:
    print(-1)
else:
    while len(answer) < a_cnt + z_cnt:
        cut_line = dp[cur_a + cur_z - 1][cur_z]
        if cut_line >= goal:
            answer += 'a'
            cur_a -= 1
        else:
            answer += 'z'
            goal -= cut_line
            cur_z -= 1
    print(answer)