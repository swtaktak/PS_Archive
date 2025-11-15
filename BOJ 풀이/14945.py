import sys
input = sys.stdin.readline
P = 10007
N = int(input())

dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 그냥은 안되고, 거리 차이의 기준으로 계산한다.
for floor in range(1, N+1):
    if floor == 1:
        dp[floor][0] = 1
    else:
        for diff in range(1, floor):
            if floor == 2:
                dp[floor][diff] = 2
            else:
                # 거리차가 줄어드는 경우는 한가지 뿐. # 거리차가 늘어나는 경우도 한가지. # 나머지는 두 가지
                dp[floor][diff] = (dp[floor-1][diff] * 2 + dp[floor-1][diff-1] + dp[floor-1][diff+1]) % P
print(sum(dp[-1]) % 10007)