import sys
input = sys.stdin.readline

# Idea / 앞에거에서 구독을 이을지, 새로 받을지

N, base = map(int, input().split())
day_list = list(map(int, input().split()))

dp = [0 for _ in range(N)]
dp[0] = base + 1

for cur in range(1, N):
    for prev in range(cur - 1, -1, -1):
        if day_list[cur] - day_list[prev] + 1 <= base:
            dp[cur] = dp[prev] + (day_list[cur] - day_list[prev])
        # 날짜를 초과했다면
        elif day_list[cur] - day_list[prev] + 1 > base:
            dp[cur] = dp[prev] + base + 1
            break
print(dp[-1])