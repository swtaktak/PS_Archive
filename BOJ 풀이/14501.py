# 14501, 15486 퇴사 1, 2
# 14501 _ bottom up으로 풀기
# i + 1 일 이후에는 그냥 일했던게 낫나, 안한게 낫나 판단
# i일차에 일하는 것을 i + 1로 고려하는 방향으로 해야 한다.
# dp만 하루 더 나간다.

N = int(input())
plan = []
for _ in range(N):
    day, money = map(int, input().split())
    plan.append((day, money))
    
dp = [0 for _ in range(N + 1)]

for cur in range(0, N):
    for next in range(cur + plan[cur][0], N+1):
        dp[next] = max(dp[next], dp[cur] + plan[cur][1])

print(dp[-1])