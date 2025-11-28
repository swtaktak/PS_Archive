import sys
input = sys.stdin.readline

N = int(input())
v = [0]  # 1-based
for _ in range(N):
    v.append(int(input()))

# dp[l][r] = l ~ r 구간만 남았을 때 얻을 수 있는 최대 이익
dp = [[0] * (N + 1) for _ in range(N + 1)]

# 길이 1부터 N까지
# 길이가 2까지 왔다는 것은.... 앞에서 자르다 이만큼 남았으므로 day는 역방향이다.
for length in range(1, N + 1):
    for left in range(1, N - length + 2):
        right = left + length - 1
        day = N - (right - left)  # 지금 몇번째 수확인가?
        if left == right:
            dp[left][right] = v[left] * day
        else:
            dp[left][right] = max(v[left] * day + dp[left + 1][right], v[right] * day + dp[left][right - 1])
print(dp[1][N])
