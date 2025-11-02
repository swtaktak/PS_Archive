import sys
input = sys.stdin.readline

while True:
    try:
        k, n = map(int, input().split())

        if k == 0 or n == 1:
            answer = 100
        else:
            dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
            for step in range(1, n + 1):
                if step == 1:
                    for num in range(0, k + 1):
                        dp[step][num] = 1
                else:
                    for num in range(0, k + 1):
                        if num == 0:
                            dp[step][num] = dp[step-1][0] + dp[step-1][1]
                        elif num == k:
                            dp[step][num] = dp[step-1][k-1] + dp[step-1][k]
                        else:
                            dp[step][num] = dp[step-1][num-1] + dp[step-1][num] + dp[step-1][num+1]
            sums = 0
            for num in range(0, k + 1):
                sums += dp[-1][num]
            answer = 100 * sums / ((k+1) ** n)
        print(f"{answer:.5f}")
    except:
        sys.exit()