import sys
input = sys.stdin.readline

# 1번 줄을 연결한다.
# 2번 줄에서 연결이 되는지 안되는지 비교..
# 3번 .....
 
N = int(input())
ropes = []
for _ in range(N):
    start, end = map(int, input().split())
    ropes.append((start, end))
ropes.sort() # start가 겹치지는 않는다.

# 최소 1줄은 이을 수 있을 것이기에
dp = [1 for _ in range(N)]
    
#  둘째줄은 비교하고.. 셋째줄을 비교하고...반복

for cur in range(1, N):
    for prev in range(0, cur):
        # 이전 상태 대비 현재 줄을 달 수 있다면
        if ropes[cur][1] > ropes[prev][1]:
            dp[cur] = max(dp[cur], dp[prev] + 1)
print(N - max(dp))