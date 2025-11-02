import sys
input = sys.stdin.readline
test_case = 1
while True:
    N = int(input())
    if N == 0:
        break
    else:
        dp = [[0, 0, 0] for _ in range(N)]
        graph = []
        for _ in range(N):
            cur_row = list(map(int, input().split()))
            graph.append(cur_row)
        for i in range(N):
            if i == 0:
                for j in range(3):
                    if j == 0:
                        dp[i][j] = 1000000
                    elif j == 1:
                        dp[i][j] = graph[i][j]
                    else:
                        dp[i][j] = graph[i][j-1] + graph[i][j]
            else:
                for j in range(3):
                    if j == 0:
                        dp[i][j] = min(dp[i-1][0], dp[i-1][1]) + graph[i][0]
                    elif j == 1:
                        dp[i][j] = min(min(dp[i-1]), dp[i][0]) + graph[i][1]
                    elif j == 2:
                        dp[i][j] = min(dp[i-1][2], dp[i-1][1], dp[i][1]) + graph[i][2]
        print("%d. %d" %(test_case, dp[-1][1]))
        test_case += 1