# 14501의 심화 버전
# bottom-up은 현재 상태를 이후에 넘겨서 O(N^2)
# 이를 미래부터 해서 반대로 풀어서 O(N)으로만들자.
import sys
input = sys.stdin.readline

N = int(input())
plan = []
for _ in range(N):
    day, money = map(int, input().split())
    plan.append((day, money))
    
dp = [0 for _ in range(N + 1)]

for prev in range(N-1, -1, -1):
    # 상담을 넘기는 것이 확정이면, 상담을 하지 않는다.
    # 그 다음 날과 동일 값
    if prev + plan[prev][0] > N:
        dp[prev] = dp[prev + 1]
    else:
        # 과거에서 상담해서 현재로 와야한다.
        # 현재 상담하고, 미래의 최대치를 받는다.
        dp[prev] = max(dp[prev + 1], plan[prev][1] + dp[prev + plan[prev][0]])
print(dp[0])