# 3 * N 타일링
import sys
input = sys.stdin.readline
N = int(input())

# 순수 2 : 3개
# 순수 4 : 2개
dp = [0] * (N + 1)
for i in range(2, N+1, 2):
    if i == 2:
        dp[2] = 3
    elif i == 4:
        dp[4] = 11
    else:
        dp[i] = 3*dp[i-2] + 2*(sum(dp[:i-3])) + 2 # 중간에 걸쳐서 계속 가는 케이스
print(dp[-1])